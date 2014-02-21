Python version: Python3.3.3

Libaries used:
bub & bar:
csv, opertor, collections, numpy, matplotlib
dashboard:
csv, opertor, collections, numpy, matplotlib and tkinter(GUI)

Dataset:
	data is extracted from "http://www.espncricinfo.com/". dataset consists of 9 countries in which player's records of each country is extrcted and we use these data for building bubble chart(Tree), bar graph.

 
bub:
	This code is 3-Dimension representation of cricket players (basically australian players, can be changed as we want) i.e., 
x-axis= total no.of matches played
y-axis= total avarage
radius of circle= total runs scored in his career.
	visualized using matplotlib
top33:
	This code is about visualising top 20 players higest scores in each country.
dashboard:
	Extension of top33 is dashboard, where we get drop down list of total countries available and user has to select one country. Selected country's top 20 players highest scores will be displayed.
