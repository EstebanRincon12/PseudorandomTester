import csv

def getListRi(csvPath):
    reader = []
    with open(csvPath, 'r') as file:
        # crear un objeto lector CSV
        myReader = csv.reader(file)

        for i in myReader:
            reader.append(float(i[0]))
    return reader