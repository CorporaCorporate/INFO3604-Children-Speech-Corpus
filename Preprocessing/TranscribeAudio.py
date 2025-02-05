import whisper
import torch
import os
# import glob
# from pydub import AudioSegment

class TranscribeAudio:


    def __init__(self, path):
        # whisper.torch.load = functools.partial(whisper.torch.load, weights_only=True)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = whisper.load_model('medium').to(self.device)
        self.filePath = path

    def transcriber(audio):
        result = audio.model.transcribe(path, fp16=False, word_timestamps=True)
        return result

    def writeFile(audio):
        result = audio.transcriber()
        fileName = os.path.basename(path)
        file = os.path.splitext(fileName)
        
        with open(file[0]+".txt", "w") as f:
            f.write(result["text"])

filePaths = [
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 2.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 3.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 4.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 5.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 6.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 7.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 8.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 5/Std 5 raw/Std 5 read 9.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 1.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 2.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 3.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 4.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 5.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read 6.wav',
    '/Users/christophegittens/Library/CloudStorage/OneDrive-SharedLibraries-TheUniversityoftheWestIndies/Phaedra Mohammed - Speech Corpora Project/Chaguanas/Std 4/Std 4 raw/Std 4 read7.wav'
    ] # paths to audio files

for path in filePaths:
    # print(path)
    audio = TranscribeAudio(path)
    audio.writeFile()
