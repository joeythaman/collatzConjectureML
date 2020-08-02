import json

import csv

oldPath = 'data'
newPath = 'data_binary'
csvEnding = '.csv'

dataCount = 1000


with open(oldPath+"_"+str(dataCount)+csvEnding, 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    csv_data = open(newPath+"_"+str(dataCount)+csvEnding, 'w')
    csvwriter = csv.writer(csv_data)

    for i in reader:
        new = []
        num = int(i[0])
        for ind in range(9,-1,-1):
            if ((1<<ind)&num):
                new.append(1)
            else:
                new.append(0)
        new.append(i[1])
        new.append(i[2])
        new.append(i[3])
        csvwriter.writerow(new)
    
    csv_data.close()

print("done")