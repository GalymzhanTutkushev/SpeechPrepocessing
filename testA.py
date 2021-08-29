# import xlrd
# import csv
# # import os
# # wav='05151sef.wav'
# # # xls = wav.replace('wav','xslx')
# # dir='/home/galymzhan/MyProjects/i-vectors/trainVAD/exl/'
# # files=os.listdir(dir)
# # xlses=filter(lambda x: x.endswith('.xlsx'),files)
# # for xls in xlses:
# #     print(dir+xls)
# #     wb = xlrd.open_workbook(dir+xls)
# #     sheet = wb.sheet_by_index(0)
# #     print(sheet.nrows)

import numpy as np 

sp=np.array([0.2, 0.9,0.9,0.9,0,0,0.9, 0.4, 0.7, 0.99,0.9,0.9,0.9,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0])
# # print(a)
sp[sp>0.8]=1
sp[sp<0.8]=0
print(sp)
# b=np.diff(a)
# print(b)

indxOne = np.where(sp==1)
print(indxOne)
lenOne = np.diff(indxOne)
lenOne = lenOne.transpose()
print(lenOne.shape)


def zero_runs(a):  # from link
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    print(ranges)
    return ranges
    
a = [34,2,3,22,22,22,22,22,22,18,90,5,-55,-19,22,6,6,6,6,6,6,6,6,23,53,1,5,-42,82]

zero_runs(np.diff(lenOne))

voiceMFCC =[]
for idx in range(labels.shape[1]:
    start = labels[idx,0]
    stop = labels[idx,1]
    voiceMFCC.extend(MFCC[start:stop,:])





# b=np.array([[2, 5, 9],[4, 3, 5]])
# print(b.shape)
# c=np.vstack((a,b))
# d=np.hstack((a,b,b))
# print(d.shape)
# # Define data
# data = [(1, "A towel,", 1.0),
#         (42, " it says, ", 2.0),
#         (1337, "is about the most ", -1),
#         (0, "massively useful thing ", 123),
#         (-2, "an interstellar hitchhiker can have.", 3)]

# # Write CSV file
# with open('test.csv', 'w') as fp:
#     writer = csv.writer(fp, delimiter=',')
#     # writer.writerow(["your", "header", "foo"])  # write header
#     writer.writerows(d)

# # Read CSV file
# with open('test.csv', 'r') as fp:
#     reader = csv.reader(fp, delimiter=',', quotechar='"')
#     # next(reader, None)  # skip the headers
#     data_read = [row for row in reader]

# print(data_read)