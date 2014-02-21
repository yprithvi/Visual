from xml.etree import ElementTree as et

import csv

#from random import randint

votes=[]

ranks=[]

with open('cinema.csv','r') as csvinput:
    for row in csv.reader(csvinput):

        try:
            if int(row[1])>=10000:
                votes.append(int(row[1]))
                ranks.append(float(row[2]))
        except ValueError:
            continue
        
#print votes

#print ranks

largeXvalue=-1

largeYvalue=-1



for each in range(0,len(votes)):
    if votes[each]>largeXvalue:
        largeXvalue=votes[each]
    if ranks[each]>largeYvalue:
        largeYvalue=ranks[each]

XAxisScalingFactor=3000.0/largeXvalue
YAxisScalingFactor=1000.0/largeYvalue

main=et.Element('svg',width='1300',height='1300',xmlns='http://www.w3.org/2000/svg',xlink='http://www.w3.org/1999/xlink')

translate=et.SubElement(main,'g',transform='translate(50,50) scale(0.5)')

axis=et.SubElement(translate,'g',style='stroke-width:5;stroke:black')

et.SubElement(axis,'path',d='M 0 1000 L 3000 1000 Z')

et.SubElement(axis,'path',d='M 0 0 L 0 1000 Z')

text_format=et.SubElement(translate,'g',style='fill:none;stroke:#B0B0B0;stroke-width:5;stroke-dasharray:2 4;text-anchor:end;font-size:30')

#HORIZONTAL DASH LINES

et.SubElement(text_format,'path',d='M 0 0 L 3000 0')

et.SubElement(text_format,'path',d='M 0 500 L 3000 500')

et.SubElement(text_format,'path',d='M 0 250 L 3000 250')

et.SubElement(text_format,'path',d='M 0 750 L 3000 750')

#VERTICAL DASH LINES

max_XValue=3000

max_YValue=1000

count=1

while count<=12:
    et.SubElement(text_format,'path',d='M '+str(250*count)+' 0 L '+str(250*count)+' 1000')
    count=count+1

"""et.SubElement(text_format,'path',d='M 3000 0 L 3000 1000')

et.SubElement(text_format,'path',d='M 2750 0 L 2750 1000')

et.SubElement(text_format,'path',d='M 1000 0 L 1000 1000')

et.SubElement(text_format,'path',d='M 1000 0 L 1000 1000')

et.SubElement(text_format,'path',d='M 1000 0 L 1000 1000')

et.SubElement(text_format,'path',d='M 500 0 L 500 1000')

et.SubElement(text_format,'path',d='M 250 0 L 250 1000')

et.SubElement(text_format,'path',d='M 750 0 L 750 1000')"""

text_format=et.SubElement(translate,'g',style='fill:black;font-size:15;stroke:none')

text=et.SubElement(text_format,'text',x='-35',y='10')

print str(largeYvalue)

text.text=str(largeYvalue)

text=et.SubElement(text_format,'text',x='-45',y='500')

text.text=str(largeYvalue*0.5)

text=et.SubElement(text_format,'text',x='-45',y='750')

text.text=str(largeYvalue*0.25)

text=et.SubElement(text_format,'text',x='-45',y='250')

text.text=str(largeYvalue*0.75)

count=12

while count>0:
    text=et.SubElement(text_format,'text',x=str((250*count)-20),y='1030')
    #print "fffff "+str(largeXvalue*(count/12.0))
    text.text=str(largeXvalue*(count/12.0))
    count=count-1

"""text=et.SubElement(text_format,'text',x='990',y='1030')

text.text=str(largeXvalue)

text=et.SubElement(text_format,'text',x='730',y='1030')

text.text=str(largeXvalue*0.75)

text=et.SubElement(text_format,'text',x='490',y='1030')

text.text=str(largeXvalue*0.5)

text=et.SubElement(text_format,'text',x='230',y='1030')

text.text=str(largeXvalue*0.25)"""

graph_format=et.SubElement(translate,'g',style='fill:none;stroke:blue;stroke-width:3')

for each in range(0,len(votes)):
    xvalue=votes[each]*XAxisScalingFactor
    yvalue=ranks[each]*YAxisScalingFactor
    yvalue=1000-yvalue

    et.SubElement(graph_format,'line',x1=str(xvalue-5),y1=str(yvalue+5),x2=str(xvalue+5),y2=str(yvalue-5))
    et.SubElement(graph_format,'line',x1=str(xvalue+5),y1=str(yvalue+5),x2=str(xvalue-5),y2=str(yvalue-5))



    
    



f=open('scatter_plot.svg','w')

f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')

f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')

f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')

#print et.tostring(main)

f.write(et.tostring(main))

f.close()


        




#main=et.Element('svg',width='1300',height='1300',id='scatter',xmlns='http://www.w3.org/2000/svg',xlink='http://www.w3.org/1999/xlink')

