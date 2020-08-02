import json
import os

filePath = 'data'
fileEnding = '.json'
step = 100

def analyze(num,count):
    s = str(num)
    if s in dic:
        return dic[s]
    if num%2 == 0:
        vals = analyze(int(num/2),count+1)
        newVals = {"turns":vals["turns"]+1,"even":vals["even"]+1,"odd":vals["odd"]}
        dic[s] = newVals
        return newVals
    else:
        vals = analyze(num*3+1,count+1)
        newVals = {"turns":vals["turns"]+1,"even":vals["even"],"odd":vals["odd"]+1}
        dic[s] = newVals
        return newVals

with open(filePath+fileEnding) as json_file:
    data = json.load(json_file)

    current = data[0]
    dic = data[1]

    for i in range(current,current+step):
        analyze(i,0)

    data[0] = current+step
    data[1] = dic

    print(data[0])

    with open(filePath+"_"+str(current+step-1)+fileEnding, 'w') as outfile:
        json.dump(data, outfile)
    with open(filePath+fileEnding, 'w') as outfile:
        json.dump(data, outfile)