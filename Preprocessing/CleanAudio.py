from scipy.io import wavfile
import noisereduce as nr
import os

class CleanAudio():

    def reduceNoise(file):
        # load data
        rate, data = wavfile.read(file)
        # perform noise reduction
        reducedNoise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.90, freq_mask_smooth_hz=400, n_std_thresh_stationary=5, n_fft=512)
        
        dirPath = os.path.dirname(file)  # Extracts the directory path only
        baseName = os.path.splitext(os.path.basename(file))[0]
        outputFile = f"{dirPath}/{baseName}_cleaned.wav"

        print(file)
        print(outputFile)

        wavfile.write(outputFile, rate, reducedNoise)