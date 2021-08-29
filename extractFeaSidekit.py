import sidekit
from sidekit.frontend.io import read_audio
from sidekit.frontend.features import mfcc
from sidekit.frontend.vad import pre_emphasis
import os
import numpy as np

directory='/home/galymzhan/Документы'
files=os.listdir(directory)
audios=filter(lambda x: x.endswith('.wav'),files)
mfcc_all=[]
for audio in audios:
    y, fs = read_audio(audio,framerate=8000)
    # print(y.ndim)
    for row in y.T:
        print(row)
        # row=row.transpose()
        # print(row)
        # yvad=pre_emphasis(input_sig=row,pre=0.97)
        # input_sig=np.trim_zeros(yvad)
        input_sig=row.transpose()

        # input_sig=row[row!=0]
        print(input_sig.shape)
        mfccs=sidekit.frontend.features.mfcc(input_sig=input_sig,nwin=0.025, nceps=13,shift=0.01, prefac=0.97)
        mfccss=np.matrix(mfccs)
        # mfcc_all.extend(mfccs)
        print(mfccss.shape)




