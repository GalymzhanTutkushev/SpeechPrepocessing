import sidekit
import os
import numpy as np 

mainDir = '/home/galymzhan/MyProjects/i-vectors'
trainDir = mainDir+'/train'
testDir = mainDir+'/test'
ubmDir = mainDir+'/ubm/wav'

models = [name for name in os.listdir(trainDir)
            if os.path.isdir(os.path.join(trainDir, name))]
testList = [x for x in os.listdir(testDir) if x.endswith(".wav")]
ubmList = [x for x in os.listdir(ubmDir) if x.endswith(".wav")]

speakerID = []
audioID = []
for model in models:
    curModWav = [x for x in os.listdir(trainDir+'/'+model) if x.endswith(".wav")]
    curMod = np.full_like(curModWav, model, dtype='U32')
    print(curMod)
    print(curModWav)

    speakerID.extend(curMod)
    audioID.extend(curModWav)


print(ubmList)
print(speakerID)
print(audioID)
idmap = sidekit.IdMap()
idmap.leftids = np.array(speakerID)
idmap.rightids = np.array(audioID)
idmap.start = np.empty_like((audioID), dtype = "|O")
idmap.stop = np.empty_like((audioID), dtype = "|O")

idmap.validate()

ndx = sidekit.Ndx()
ndx.modelset = np.array(models)
ndx.segset = np.array(testList)
ndx.trialmask = np.ones((len(models),len(testList)), dtype='bool')
print(ndx.trialmask.shape)

ndx.validate()