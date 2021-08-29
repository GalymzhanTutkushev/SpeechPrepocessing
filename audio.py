from scipy.io import wavfile as wav 
import os
import matplotlib.pyplot as plt
import scipy
import librosa
import numpy as np

directory='/home/galymzhan/Документы'
files=os.listdir(directory)
for file in files:
     print(file)
     print(os.path.isdir(file))
     print(os.path.isfile(file))
audios=filter(lambda x: x.endswith('.wav'),files)
for audio in audios:
     print(audio)
     rate, data = scipy.io.wavfile.read(audio)
     y, sr = librosa.load(audio)
     mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
     mfcc_delta = librosa.feature.delta(mfccs)
     mfcc_delta2 = librosa.feature.delta(mfccs, order=2)
     mfcc39= mfccs.apend(mfcc_delta)
     print(len(mfcc39))
     can1 = data[:,1]
     plt.figure()
     plt.plot(can1)
     plt.show()
