
import urllib
import datetime
import csv
import urllib2
import re

company_url="http://ichart.finance.yahoo.com/table.csv?"
BASE_URL='http://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S.26P_500_Component_Stocks'
reg='^<td><a rel="nofollow" class="external text" .*>([A-Z]{1,})</a></td>'


response = urllib2.urlopen(BASE_URL)
html = response.read()
com_tags=html.split('\n')
#print com_li
cop_for=re.compile(reg)
com_li=[]
#text_file=open("company_names.txt","w")
#text_file.write("start:\n")
for each in com_tags:
    names=cop_for.match(each)
    if names!=None:
        #print str(names.group(1))
        com_li.append(str(names.group(1)))
print com_li


today=datetime.date.today()
starting=today-datetime.timedelta(days=30)

sdate=str(int(starting.strftime('%d')))
smonth=str(int(starting.strftime('%m'))-1)
syear=str(int(starting.strftime('%Y')))
    
edate=str(int(today.strftime('%d')))
emonth=str(int(today.strftime('%m'))-1)
eyear=str(int(today.strftime('%Y')))

date_url="&a="+smonth+"&b="+sdate+"&c="+syear+"&d="+emonth+"&e="+edate+"&f="+eyear+"&g=d&ignore=.csv"
print date_url
for each in com_li:
    main_url=company_url+"s="+each+date_url
    u = urllib2.urlopen(main_url)
    with open('Companies\\'+each+'.csv',"w") as csv:
        csv.write(u.read())
        csv.close()
