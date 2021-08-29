from getFilenames import *
import extractMFCC
mainDir='/home/galymzhan/Документы'
trainDir=mainDir+'/'
testDir=mainDir+'/'
trainFiles = getTrainfiles(trainDir)
testFiles = getTestfiles(trainDir)
trainMFCC = extractMFCC(trainFiles)
