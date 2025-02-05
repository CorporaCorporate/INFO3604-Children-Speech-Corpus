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

'''

@article{sainburg2020finding,
  title={Finding, visualizing, and quantifying latent structure across diverse animal vocal repertoires},
  author={Sainburg, Tim and Thielk, Marvin and Gentner, Timothy Q},
  journal={PLoS computational biology},
  volume={16},
  number={10},
  pages={e1008228},
  year={2020},
  publisher={Public Library of Science}
}

@software{tim_sainburg_2019_3243139,
  author       = {Tim Sainburg},
  title        = {timsainb/noisereduce: v1.0},
  month        = jun,
  year         = 2019,
  publisher    = {Zenodo},
  version      = {db94fe2},
  doi          = {10.5281/zenodo.3243139},
  url          = {https://doi.org/10.5281/zenodo.3243139}
}


'''