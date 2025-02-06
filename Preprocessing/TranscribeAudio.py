import whisper
import torch
import os
import SplitAudio as splitAudio
# import glob
# from pydub import AudioSegment

class TranscribeAudio():

    def __init__(self, path):
        # whisper.torch.load = functools.partial(whisper.torch.load, weights_only=True)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = whisper.load_model('medium').to(self.device)
        self.path = path
        self.directories = []
        self.rootdir = '/Users/christophegittens/Library/CloudStorage/OneDrive-TheUniversityoftheWestIndies,St.Augustine/Speech Corpus/Chaguanas/Std 2' #insert root dir here

    def transcriber(self):
        result = self.model.transcribe(self.path, fp16=False, word_timestamps=True)
        return result

    def writeFile(self):
        result = self.transcriber()
        fileName = os.path.basename(self.path)
        file = os.path.splitext(fileName)
        
        with open(file[0]+".txt", "w") as f:
            f.write(result["text"])
    
    def transcribeSplices(self):
        i = 0
        for subdir, dirs, files in os.walk(self.directories[i]):
            for file in files:
                if '_cleaned' in file:
                    audio = TranscribeAudio(os.path.join(subdir, file))
                    audio.writeFile()
            i+=1

    @staticmethod
    def splitAndCleanAudio():
        transcribeAudio = TranscribeAudio(None)
        for subdir, dirs, files in os.walk(transcribeAudio.rootdir):
            if 'comp' in subdir:
                for file in files:
                    if '.wav' in file:
                        path = os.path.join(subdir, file)
                        newPath, newDir = splitAudio.SplitAudio.splitAudio(path)
                        transcribeAudio.directories.append(newDir)
        
        return transcribeAudio
    
transcribeAudio = TranscribeAudio(None).splitAndCleanAudio()
transcribeAudio.transcribeSplices()              