from django.core.management.base import BaseCommand, CommandError
from django.conf import  settings
from django.core.management import call_command
import json
class Command(BaseCommand):
	
	args = ''
	
	help = 'loads the initial data into database'
	
	def  handle(self, *args, **options):
		call_command('loaddata', 'Rainfall-England.json', verbosity=0)
		result = {'message': "Successfully Loading initial data"}
		return  json.dumps(result)
		
call_command('loaddata', 'Rainfall-England.json', verbosity=0)
result = {'message': "Successfully Loading initial data"}
json.save(result)