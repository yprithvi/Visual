import csv
import operator
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt

listofcountries=['england','australia','south Africa','west indies','New zealand','india','pakistan','sri lanka','zimbambwe']
#for i in listofcountries:
with open("Countries//australia.csv") as f:
    reader = csv.reader(f)
    players=[]
    
    for row in reader:
        #players.append(row[0])
        alli=[]
        
        if (row[6]=="-" or row[4]=="-"):
            pass
        else:
            alli.append(row[0])
            alli.append(float(row[6]))
            alli.append(int(row[4]))
            alli.append(int(row[1]))
        
             
        #print x
        if (len(alli)!=0):
            players.append(alli)

        #plt.text(float(row[6]), int(row[4]), row[0], size=8, horizontalalignment='center')
#print players
x=[]
y=[]
size=[]
for i in players:
    if (i[3]>150):
        plt.text(i[3], i[1], i[0], size=8, horizontalalignment='center')
    x.append(i[3])
    y.append(i[1])
    size.append(i[2])
#print x
#print y
#print size
#print players

plt.scatter(x,y, s=size, marker='o', c=size, linewidths=2, edgecolor='w')
plt.savefig("bubble.png")
plt.show()

