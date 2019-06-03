
from docx import Document
import csv
listm = []
listf = []
def ReadDocuement():
    wordDoc = Document('C:/Users/pc/Desktop/data.docx')
    for table in wordDoc.tables:
        for row in table.rows:
            try:
                if row.cells[0].text != '' and row.cells[0].text != 'Nombre' and row.cells[1].text != ''  and row.cells[1].text != 'Sexo':
                    if row.cells[1].text.lower() == 'f':
                        if row.cells[0].text.lower() != '' and row.cells[0].text.lower() != 'f' and row.cells[0].text.lower() != 'm':
                            listf.append("'"+row.cells[0].text.lower()+"',")
                    else:
                        if row.cells[0].text.lower() != '' and row.cells[0].text.lower() != 'f' and row.cells[0].text.lower() != 'm':
                            listm.append("'"+row.cells[0].text.lower()+"',")
            except:
                print ('Error')

def WriteDocuemt():
    file = open('testfile.txt','w') 
    for x in listm:
        file.write(x)
    file.write("\n\n\n\n\n")
    for x in listf:
        file.write(x)

file = open('C:/Users/pc/Desktop/PYTHON/testfile.txt','r')
listm = file.readlines()
print(len(listm))
print(listm)
c= 0
for x in listm:
    print("'"+x.lower().replace('\n','')+"'",end=",")

    if c == 9:
        c = 0
    else:
        c+=1
