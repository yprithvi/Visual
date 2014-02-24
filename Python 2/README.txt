python version: python 2.7

libraries need for these codes:
ElementTree, numpy, scipy, csv, operator, os, re, urllib, datetime, matplotlib
If using windows, You can download packages from : http://www.lfd.uci.edu/~gohlke/pythonlibs/


scrap:
	This code is to extract data into csv file:
	from url='http://en.wikipedia.org/wiki/List_of_S%26P_500_companies' we get 500 company names and from those each company names we extract each companies 	finance details by adding company name and date to url: "http://ichart.finance.yahoo.com/table.csv?"
	and each estracted data is stored in companies folder.

correlation matrix: (data: Month_CSVs)
	month_csv folder consists of 3881 companies based on bse code.
	among those files, column 4 is about stocks of particular area for each day in a month, using this values we are finding out correltion between first 30 	companies.


scatter plot:(data: cinema.csv)
	cinema.csv consists of various fields like votes, rank and title(mainly) using no.of votes(x-axis) vs rank visualized a scatter plot.


cormatrix: (data: allcountries)
	Data is about exchange rate of each country according to Indian currency

	This code is based upon finding the correlation between 30 countries currency rate change with respective to India. Representing correlation between them in 	svg file.
	ln:25-80
		Writing basic outline of svg file with values from "Task2()"(Ln:82)

	Ln:107
		using numpy library, using function corrcoef funtion finding out the correlation values between those both values.


These SVG files are created by executing the codes provided. As this code needs libraries and correct file paths to the datasets, these codes may produce runtime errors. 
