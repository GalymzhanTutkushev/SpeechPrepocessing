import xlrd
import os
directory='/home/galymzhan/Документы'
files=os.listdir(directory)
xlses=filter(lambda x: x.endswith('.xlsx'),files)
for xls in xlses:
     print(xls)
     wb = xlrd.open_workbook(xls)
     sheet = wb.sheet_by_index(0)
     sheet.cell_value(0,0)
     print(sheet.nrows)
     print(sheet)
    #  for i in range(sheet.nrows):
        #  print(sheet.row_values(i))
