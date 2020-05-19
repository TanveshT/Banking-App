import csv
from os import listdir
import fnmatch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dictType = {}
x = []
y = []
print "\n"
l = listdir("/home/kirisaki/internship - atpof/training - python/UIusingCLasses")
pattern = "*.csv"
print "CHOOSE THE FILE FROM WHICH YOU NEED TO ANALYSE:-"
for entry in l:
    if fnmatch.fnmatch(entry, pattern):
        print entry

filename = raw_input("ENTER THE EXACT NAME OF THE FILE:")

with open(filename, "r") as AnalysisCSV:

    AnalysisCSV.seek(0)
    csvReader = csv.reader(AnalysisCSV, delimiter=',')
    for row in csvReader:
        dictType[row[4]] = 0

    AnalysisCSV.close()

with open(filename, "r") as AnalysisCSV:

    AnalysisCSV.seek(0)
    csvReader = csv.reader(AnalysisCSV, delimiter=',')
    for row in csvReader:
        if row[4] in dictType:
            dictType[row[4]] += 1

    AnalysisCSV.close()

df = pd.DataFrame(dictType,index = ["Number Of Transactions"])

print dictType

points =[]
m = 1
for i in dictType:
    x.append(i)
    y.append(dictType[i])
    points.append(m)
    m+=1

plt.xticks(points, x)

plt.bar(points,y)
plt.xlabel("TYPE OF TRANSACTIONS")
plt.ylabel("NUMBER OF TRANSACTIONS")
plt.show()

df = pd.read_csv(filename)
print
print df
print
df["Type"] = df["Type"].fillna("ONLINE TRANSACTION")
print df

x = list(df["DATE"])
points = np.arange(1,len(x)+1,1)
y = list(df["Amount"])
plt.xticks(points, x)
plt.xticks(rotation = 'vertical')

plt.plot(points,y)
plt.tight_layout()
plt.xlabel("TYPE OF TRANSACTIONS")
plt.ylabel("NUMBER OF TRANSACTIONS")
plt.show()
