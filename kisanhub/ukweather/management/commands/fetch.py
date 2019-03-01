
import requests
from django.core.management import BaseCommand
class Command(BaseCommand):
	
	def handle(*args, **options):
		metrics = ['Tmax', 'Tmin', 'Rainfall']
		locations = ['UK', 'England', 'Scotland', 'Wales']
		data=[]
		for metric in metrics:
			for location in locations:
				print(metric)
				print(location)
				a=requests.get('https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/%s-%s.json'%(metric,location))
				d=a.json()
				data.append(d)		
				value=[]
				year=[]
				month=[]
				for i in range(3):
					value.append(d[i]['value'])
					year.append(d[i]['year'])
					month.append(d[i]['month'])
					print(year[i],month[i], value[i] )
					print(data)
				
		
