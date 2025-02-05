import sys
import subprocess
import os

class SplitAudio:
    
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
    def splitAudio(originalTrack, segmentLength=150):
        if not os.path.exists(originalTrack):
            print(f"Error: File '{originalTrack}' not found.")
            sys.exit(1)

        SplitAudio.checkffmpeg()
        duration = SplitAudio.getAudioDuration(originalTrack)
        outputFormat = SplitAudio.getOutputFormat(originalTrack)

        numSegments = int(duration // segmentLength) + 1  # Round up to cover last segment

        for i in range(numSegments):
            startTime = i * segmentLength
            outputFile = f"{os.path.splitext(originalTrack)[0]}_part{i+1}.{outputFormat}"

            command = f'ffmpeg -i "{originalTrack}" -acodec copy -ss {startTime} -t {segmentLength} "{outputFile}"'

            print(f"Creating: {outputFile} ({startTime}s - {startTime + segmentLength}s)")
            subprocess.run(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_audio.py <original_track>")
        sys.exit(1)

splitAudio = SplitAudio()
splitAudio.splitAudio(sys.argv[1])