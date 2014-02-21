from xml.etree import ElementTree as et
import numpy as np
import csv
import os
import re

INPUT_DIR="Month_CSVs"

pattern="^([\d]+).csv"

comp_format=re.compile(pattern)

count=0

company_count=0

company_list=[]
stock_list=[]
stock_values=[]

for filename in os.listdir(INPUT_DIR):
    with open(os.path.join(INPUT_DIR,filename)) as eachfile:
        reader=csv.reader(eachfile)
        if count==30:
            company_list.append(result.group(1))
            stock_list.append(stock_values)
            company_count=company_count+1
        if company_count==30:
            break
        count=0
        stock_values=[]
        #print len(reader)
        result=comp_format.match(filename)
        for row in reader:
            try:
                
                #company_stock[result.group(1)].append(float(row[4]))
                stock_values.append(float(row[4]))
                count=count+1
            except ValueError:
                #company_stock[result.group(1)]=[float(row[4])]
                continue



correlation_matrix=[]



for each in stock_list:
    corr_each=[]
    for other in stock_list:
        corr_each.append(np.corrcoef(each,other)[0][1])
    correlation_matrix.append(corr_each)



#print correlation_matrix




def construct_svg():
    
    main=et.Element('svg',width='1300',height='1300',xmlns='http://www.w3.org/2000/svg',xlink='http://www.w3.org/1999/xlink')

    #et.SubElement(main,'rect',width='30',height='30',style='fill:rgb(255,240,240)')

    translate=et.SubElement(main,'g',transform='translate(100,100) scale(0.5)')

    

    axis=et.SubElement(translate,'g',style='stroke-width:5;stroke:black')

    et.SubElement(axis,'path',d='M 0 900 L 900 900 Z')

    et.SubElement(axis,'path',d='M 0 0 L 0 900 Z')

    positive_range=['rgb(235,255,235)','rgb(225,255,225)','rgb(215,255,215)','rgb(205,255,205)','rgb(190,255,190)','rgb(175,255,175)','rgb(160,255,160)','rgb(145,255,145)','rgb(125,255,125)','rgb(100,255,100)','rgb(0,255,0)']
    
    negative_range=['rgb(255,235,235)','rgb(255,225,225)','rgb(255,215,215)','rgb(255,205,205)','rgb(255,190,190)','rgb(255,175,175)','rgb(255,160,160)','rgb(255,145,145)','rgb(255,125,125)','rgb(255,100,100)','rgb(255,0,0)']
    
    grid_format=et.SubElement(translate,'g',style='fill:none;stroke:#B0B0B0;stroke-width:5;stroke-dasharray:2 4;text-anchor:end;font-size:30')

    count=1

    while count<=30:
        et.SubElement(grid_format,'path',d='M '+str(30*count)+' 0 L '+str(30*count)+' 900')
        count=count+1

    count=0

    while count<30:
        et.SubElement(grid_format,'path',d='M 0 '+str(30*count)+' L 900 '+str(30*count))
        count=count+1

    x_point=0
    y_point=0

    pattern='0[.](\d)'
    num_format=re.compile(pattern)

    
    for each_list in correlation_matrix:
        for each in each_list:
            if each==1:
                et.SubElement(translate,'rect',x=str(x_point),y=str(y_point),width='30',height='30',style='fill:rgb(0,255,0);stroke:#B0B0B0;stroke-width:2')
            elif each==0:
                et.SubElement(translate,'rect',x=str(x_point),y=str(y_point),width='30',height='30',style='fill:rgb(0,0,255);stroke:#B0B0B0;stroke-width:2')
            elif each==-1:
                et.SubElement(translate,'rect',x=str(x_point),y=str(y_point),width='30',height='30',style='fill:rgb(255,0,0);stroke:#B0B0B0;stroke-width:2')
            elif each<0:
                #print each
                result=num_format.search(str(each))
                value=int(result.group(1))
                et.SubElement(translate,'rect',x=str(x_point),y=str(y_point),width='30',height='30',style='fill:'+negative_range[value]+';stroke:#B0B0B0;stroke-width:2')
            elif each>0:
                #print each
                result=num_format.search(str(each))
                value=int(result.group(1))
                et.SubElement(translate,'rect',x=str(x_point),y=str(y_point),width='30',height='30',style='fill:'+positive_range[value]+';stroke:#B0B0B0;stroke-width:2')
            x_point=30+x_point
        x_point=0
        y_point=y_point+30
            
            
    et.SubElement(translate,'rect',x='1200',y='0',width='40',height='40',style='fill:rgb(0,255,0);stroke:#B0B0B0;stroke-width:2')        
    
    

    count=9
    y_point=50

    while count>=0:
        et.SubElement(translate,'rect',x='1200',y=str(y_point),width='40',height='40',style='fill:'+positive_range[count]+';stroke:#B0B0B0;stroke-width:2')
        y_point=y_point+40
        count=count-1
    

    et.SubElement(translate,'rect',x='1200',y=str(y_point+10),width='40',height='40',style='fill:rgb(0,0,255);stroke:#B0B0B0;stroke-width:2')

    count=0

    y_point=y_point+60
    
    while count<10:
        et.SubElement(translate,'rect',x='1200',y=str(y_point),width='40',height='40',style='fill:'+negative_range[count]+';stroke:#B0B0B0;stroke-width:2')
        y_point=y_point+40
        count=count+1

    et.SubElement(translate,'rect',x='1200',y=str(y_point+10),width='40',height='40',style='fill:rgb(255,0,0);stroke:#B0B0B0;stroke-width:2')

    text_format=et.SubElement(translate,'g',style='fill:black;font-size:20;stroke:none')
    text=et.SubElement(text_format,'text',x='1245',y='20')
    text.text='1'

    count=9
    y_point=70

    while count>=0:
        text=et.SubElement(text_format,'text',x='1245',y=str(y_point))
        text.text='0.'+str(count)
        count=count-1
        y_point=y_point+40

    #text_format=et.SubElement(translate,'g',style='fill:black;font-size:20;stroke:none')
    text=et.SubElement(text_format,'text',x='1245',y=str(y_point+20))
    text.text='0'

    count=0
    y_point=y_point+60

    while count<10:
        text=et.SubElement(text_format,'text',x='1245',y=str(y_point))
        text.text='-0.'+str(count)
        count=count+1
        y_point=y_point+40

    
    text=et.SubElement(text_format,'text',x='1245',y=str(y_point+20))
    text.text='-1'

    names_dic={}

    with open('EQ081113.csv','r') as company_name:
        names_list=csv.reader(company_name)
        count=0
        for row in names_list:
            count=count+1
            if count==1:
                continue
            names_dic[row[0]]=row[1]
            

    #print names_dic
            
    count=0

    text_format=et.SubElement(translate,'g',style='fill:black;font-size:20;stroke:none')
    y_point=8
    x_point=5

    while count<30:
        texty=et.SubElement(text_format,'text',x='-150',y=str(y_point))
        textx=et.SubElement(text_format,'text',x=str(x_point),y='920',transform='rotate(45,'+str(x_point)+',920)')
        textx.text=names_dic[company_list[count]]
        texty.text=names_dic[company_list[count]]
        x_point=x_point+30
        y_point=y_point+30
        count=count+1
    
            
    
        

    f=open('correlation_matrix.svg','w')

    f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')

    f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')

    f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')

#print et.tostring(main)

    f.write(et.tostring(main))

    f.close()
    
construct_svg()    
    
    


