import whisper
import torch
import os
import SplitAudio as splitAudio
# import glob
# from pydub import AudioSegment

class TranscribeAudio():

    def __init__(self, path, rootdir):
        # whisper.torch.load = functools.partial(whisper.torch.load, weights_only=True)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = whisper.load_model('medium').to(self.device)
        self.path = path
        self.directories = []
        self.rootdir = rootdir

    def transcriber(self):
        result = self.model.transcribe(self.path, fp16=False, word_timestamps=True)
        return result

    def writeFile(self):
        result = self.transcriber()
        fileName = os.path.basename(self.path)
        file = os.path.splitext(fileName)
        folderPath = os.path.join(rootdir, "Transcriptions")
        filePath = os.path.join(folderPath, file[0] + ".txt")

        print("filename: ", fileName, "file: ", file)

        # create the folder if it doesn't exist 
        if not os.path.exists(folderPath): 
            os.makedirs(folderPath) 
        
        # filePath = os.path.join(folderPath, fileName+".txt")
        
        with open(filePath, "w") as f:
            f.write(result["text"])
    
    def transcribeSplices(self, rootdir):
        for dir in self.directories:
            for subdir, dirs, files in os.walk(dir):
                for file in files:
                    if '.wav' in file:
                        audio = TranscribeAudio(os.path.join(subdir, file), rootdir)
                        audio.writeFile()
                        # print(file)
                        # print(dir)

    @staticmethod
    def splitAndCleanAudio(rootdir):
        transcribeAudio = TranscribeAudio(None, rootdir)
        for subdir, dirs, files in os.walk(transcribeAudio.rootdir):
            if 'comp' in subdir:
                for file in files:
                    if '.wav' in file:
                        path = os.path.join(subdir, file)
                        newPath, newDir = splitAudio.SplitAudio.splitAudio(path)
                        transcribeAudio.directories.append(newDir)
        
        return transcribeAudio
    
rootdir = '/Users/christophegittens/Library/CloudStorage/OneDrive-TheUniversityoftheWestIndies,St.Augustine/Speech Corpus/Chaguanas/Std 2' #insert root dir here

if __name__ == "__main__":
    transcribeAudio = TranscribeAudio(None, rootdir).splitAndCleanAudio(rootdir)
    transcribeAudio.transcribeSplices(rootdir)