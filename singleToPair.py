import json

import csv

oldPath = 'data'
newPath = 'data_pair'
csvEnding = '.csv'

dataCount = 10000


with open(oldPath+"_"+str(dataCount)+csvEnding, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    lis = []
    for i in reader:
        lis.append(i)

    csv_data = open(newPath+"_"+str(1000)+csvEnding, 'w')
    csvwriter = csv.writer(csv_data)
    for i1 in range(1,1001):
        row1 = lis[i1]
        print(row1)
        for i2 in range(1,1001):
            row2 = lis[i2]
            turnVal = 0
            if int(row2[1]) > int(row1[1]):
                turnVal = 1
            evenVal = 0
            if int(row2[2]) > int(row1[2]):
                evenVal = 1
            oddVal = 0
            if int(row2[3]) > int(row1[3]):
                oddVal = 1
            csvwriter.writerow([int(row1[0]),int(row2[0]),turnVal,evenVal,oddVal])
    
    csv_data.close()

print("done")