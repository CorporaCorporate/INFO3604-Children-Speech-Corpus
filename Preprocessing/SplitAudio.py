import sys
import subprocess
import os
import CleanAudio as cleanAudio

class SplitAudio():
    
    @staticmethod
    def checkffmpeg():
        try:
            subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except FileNotFoundError:
            print("Error: FFmpeg is not installed. Install it and try again.")
            sys.exit(1)

    @staticmethod
    def getAudioDuration(filename):
        try:
            result = subprocess.run(
                ["ffprobe", "-i", filename, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
            )
            return float(result.stdout.strip())
        except Exception as e:
            print(f"Error getting duration: {e}")
            sys.exit(1)

    @staticmethod
    def getOutputFormat(originalTrack):
        return os.path.splitext(originalTrack)[-1][1:] # Removes the dot (e.g., "wav" from ".wav")

    @staticmethod
    def splitAudio(originalTrack, segmentLength=120):
        if not os.path.exists(originalTrack):
            print(f"Error: File '{originalTrack}' not found.")
            sys.exit(1)

        SplitAudio.checkffmpeg()
        print(originalTrack)
        duration = SplitAudio.getAudioDuration(originalTrack)
        outputFormat = SplitAudio.getOutputFormat(originalTrack)


        baseName = os.path.splitext(os.path.basename(originalTrack))[0]

        outputFolder = os.path.join(os.path.dirname(originalTrack), baseName)
        os.makedirs(outputFolder, exist_ok=True)

        numSegments = int(duration // segmentLength) + 1  # Round up to cover last segment

        for i in range(numSegments):
            startTime = i * segmentLength
            outputFile = os.path.join(outputFolder, f"{baseName}_part{i+1}.{outputFormat}")

            command = f'ffmpeg -i "{originalTrack}" -acodec copy -ss {startTime} -t {segmentLength} "{outputFile}"'

            print(f"Creating: {outputFile} ({startTime}s - {startTime + segmentLength}s)")
            subprocess.run(command, shell=True)
            outputFile = SplitAudio.noiseReducer(outputFile, i)

        return outputFile, outputFolder

    @staticmethod
    def noiseReducer(file, i):
        cleanAudio.CleanAudio.reduceNoise(file)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python SplitAudio.py <original_track>")
        sys.exit(1)

# splitAudio = SplitAudio()
# splitAudio.splitAudio(sys.argv[1])