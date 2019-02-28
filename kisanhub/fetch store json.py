import requests

a=requests.get('https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-England.json')

d=a.json()
value=[]
year=[]
month=[]
all=[]

for i in range(len(d)):
	value.append(d[i]['value'])
	year.append(d[i]['year'])
	month.append(d[i]['month'])
	print(year[i],month[i], value[i] )

