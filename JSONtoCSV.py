import json

import csv

filePath = 'data'
jsonEnding = '.json'
csvEnding = '.csv'

dataCount = 1000

with open(filePath+"_"+str(dataCount)+jsonEnding) as json_file:
    data = json.load(json_file)
    data = data[1]
    
    csv_data = open(filePath+"_"+str(dataCount)+csvEnding, 'w')
    csvwriter = csv.writer(csv_data)
    
    for i in range(1,dataCount+1):
        j = str(i)
        csvwriter.writerow([i,data[j]["turns"],data[j]["even"],data[j]["odd"]])

    csv_data.close()

print("done")