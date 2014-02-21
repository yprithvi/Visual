import csv
import operator
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt

listofcountries=['england','australia','south Africa','west indies','New zealand','india','pakistan','sri lanka','zimbambwe']
#for i in listofcountries:
with open(r"Countries//england.csv") as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    players={}
    
    for row in reader:
        x=row[5].replace("*","")        
        #print (x)
        if(x=="-"):
            players[row[0]]=0
        else:
            #print (x)
            players[row[0]]=int(x)
            #print (x)
    #print (players)

blah=(players.items())
#print (players.values())
#print(sorted(blah, key=lambda item: (-item[1], item[0])))
newlist= sorted(blah, key=lambda item: (-item[1], item[0]))[:20]
print (newlist)
#print (newlist)
z=range(0,20)
#print x
y=[]
x=[]
for i in newlist:
    x.append(i[0])
    y.append(float(i[1]))
print (y)
print (x)
#plt.text(z, y, )
plt.bar(z,y)
#plt.yticks(y)
plt.xticks(z,x, rotation=80)

plt.show()
