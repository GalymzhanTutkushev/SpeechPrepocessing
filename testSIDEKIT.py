import sidekit
from sidekit.frontend.features import mfcc
from sidekit.frontend.io import read_audio
import numpy as np
y, fs = sidekit.frontend.io.read_audio('3.wav',framerate=8000)
print(fs)
yvad=sidekit.frontend.vad.pre_emphasis(input_sig=y[:,0],pre=0.97)
input_sig=np.trim_zeros(yvad)
input_sig=yvad[yvad!=0]
# input_sig=yvad
print(input_sig.shape)
mfcc=sidekit.frontend.features.mfcc(input_sig=input_sig)
print(mfcc)
# delta=sidekit.frontend.compute_delta(features=mfcc,win=3,method='filter')
# print(y)