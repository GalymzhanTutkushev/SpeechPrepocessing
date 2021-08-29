
import os
def getTrainfiles(directory):
    files=os.listdir(directory)
    for file in files:
     print(file)
     print(os.path.isdir(file))
     print(os.path.isfile(file))
audios=filter(lambda x: x.endswith('.wav'),files)

