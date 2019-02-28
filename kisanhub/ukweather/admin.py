from django.contrib import admin

# Register your models here.
from . models import Weather

class WeatherAdmin(admin.ModelAdmin):
	list_display = ['value', 'year', 'month']
	
admin.site.register(Weather,WeatherAdmin)
