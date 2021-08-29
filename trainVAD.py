import sidekit
import os
import numpy as np 
import xlrd
from sidekit.frontend.io import read_audio
from sidekit.frontend.features import mfcc
from sidekit.frontend.features import compute_delta
import csv

mainDir = '/home/galymzhan/MyProjects/i-vectors'
wavDir = mainDir + '/trainVAD/'
exlDir = wavDir + '/exl/'
allFea = []
allSpe = []
wavList = [x for x in os.listdir(wavDir) if x.endswith(".wav")]

for wav in wavList:                                  #цикл по файлам
    y, fs = read_audio(wavDir + wav,framerate=8000)  
    xls = wav.replace('wav','xslx')
    wb = xlrd.open_workbook(exlDir + xls)      
    for i in range(2):                               #цикл по каналам
        sheet = wb.sheet_by_index(i)
        print(sheet.nrows)
        y_chan = y[:,i]
        for j in range(sheet.nrows):                 #цикл по блокам
            print(sheet.row_values(j))
            begin = sheet.cell_value(j,0)
            end = sheet.cell_value(j,1)
            y_seg = y_chan[begin:end]
            mfccs = mfcc(input_sig=y_seg,nwin=0.025, nceps=13,shift=0.01, prefac=0.97)
            delta = compute_delta(mfccs)
            deltaDelta = compute_delta(delta)
            fea = np.hstack((mfccs,delta,deltaDelta))
            allFea = np.vstack((allFea,fea))
            
            speech = sheet.cell_value(j,3)
            if speech:
                vad_classes = np.ones(mfccs.shape(),1)
            else:
                vad_classes = np.zeros(mfccs.shape(),1)
            
            allSpe = np.vstack((allSpe,speech))
            

# Write MFCC
with open('inputMFCC.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',')
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(allFea)

# Write speechFlags
with open('targetSpeech.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',')
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(allSpe)



                                                    

