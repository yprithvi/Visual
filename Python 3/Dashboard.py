import csv
import operator
from collections import OrderedDict
import numpy as np

from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

root=Tk()
root.title("blah")

def ploting():
    #print ('hi')
    x=country.get()
    print (x)
    with open(r"Countries//"+x+".csv") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        players={}
        for row in reader:
            x=row[5].replace("*","")        
            if(x=="-"):
                players[row[0]]=0
            else:
                players[row[0]]=int(x)
    blah=(players.items())
    newlist= sorted(blah, key=lambda item: (-item[1], item[0]))[:20]
    z=range(0,20)
    y=[]
    x=[]
    for i in newlist:
        x.append(i[0])
        y.append(float(i[1]))
    f = Figure(figsize=(6,5), dpi=125)
    a = f.add_subplot(111)
    #a = f.add_axes(x)
    a.bar(z,y)
    
    canvas = FigureCanvasTkAgg(f, master=frame2)
    canvas.get_tk_widget().grid(row=1, column=1)
    
    #mywid(frame2).grid(column=0, row=0, sticky=W+E)
    #pass

def submitForm():
    x=country.get()
    results='australia'
    label1 = ttk.Label(frame2, text=results).grid(column=0, row=0, sticky=W+E)
    print(x)
    #pass

frame1=ttk.Frame(root, padding="3 3")
frame2=ttk.Frame(root, height=500, width=500, padding="3 3")
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)


frame1.grid(column=0, row=0, sticky=(N, W, E, S))
frame2.grid(column=1, row=0, sticky=(N, W, E, S))

frame1['borderwidth']=2
frame1['relief']="raised"
frame2['borderwidth']=2
frame2['relief']="sunken"

resultsContents = "Plotting"
print (resultsContents)
label = ttk.Label(frame2, text=resultsContents).grid(column=0, row=0, sticky=W+E)


countryvar = StringVar()
lis=['england','australia','india', 'New zealand', 'pakistan', 'south Africa', 'sri lanka', 'west indies', 'zimbabwe']

country = ttk.Combobox(frame1, textvariable=countryvar, values=lis)
country.set(lis[2])
country.pack()
country.grid(column=0, row=0, sticky=N)
#x=country.get()
#print(x)
#country.bind('<<ComboboxSelected>>', submitForm)
#country.pack()
#country['values']=('England', 'Australia', 'India')
#
#image = PhotoImage(file='example.png')
#label['image'] = image

button = ttk.Button(frame1, text='Okay', command=ploting).grid(column=0, row=1, sticky=N+W+E)


root.mainloop();
