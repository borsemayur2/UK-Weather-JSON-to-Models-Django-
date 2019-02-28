from django.db import models
import json
# Create your models here.
class Weather(models.Model):
	value = models.FloatField()
	year = models.IntegerField()
	month = models.IntegerField()

class Locations(models.Model):
	name = models.CharField(max_length=100)
	
#	def __str__(self):
#		return self.value

'''def jsontoclass(self, aux):
		self.name=aux['name']
		self.username = aux['username']
s={
    "username": "clelio",
    "name": "Clelio de Paula",
}

w=Weather()

w.jsontoclass(s)'''