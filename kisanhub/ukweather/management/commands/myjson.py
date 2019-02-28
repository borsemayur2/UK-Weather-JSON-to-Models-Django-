"""
Import json data from URL to Datababse
"""
import requests
import json
from ... models import Weather
from django.core.management.base import BaseCommand





class Command(BaseCommand):

    
    def import_weather(self, data):
        value = data.get('value', None)
        month = data.get('month', None)
        year = data.get('year', None)

        try:
            weather, created = Weather.objects.get_or_create(
                value=value,
                month=month,
                year = year
            )
            if created:
                weather.save()
                display_format = " {}, has been saved."
                print(display_format.format(weather))
        except Exception as ex:
            print(str(ex))
            msg = "\n\nSomething went wrong saving this movie: {}\n{}".format(value, str(ex))
            print(msg)


    def handle(self, *args, **options):
        """
        Makes a GET request to the  API.
        """
        metrics = ['Tmax', 'Tmin', 'Rainfall']
        locations = ['UK', 'England', 'Scotland', 'Wales']
        dicct = {"metric":['Tmax','Tmin','Rainfall'],
        "location":['UK','England','Scotland','Wales']}
        for location in locations:
            for metric in metrics:
                IMPORT_URL = 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/%s-%s.json'%(metric, location)
                print(location,'-',metric)
                for num in range(12):
                    headers = {'Content-Type': 'application/json'}
                    response = requests.get(url=IMPORT_URL, headers=headers,)

        response.raise_for_status()
        data = response.json()

        for data_object in data:
            self.import_weather(data_object)
