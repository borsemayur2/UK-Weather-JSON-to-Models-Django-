from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Weather
from  . serializers import WeatherSerializer


# Create your views here.
class WeatherList(APIView):
	
	def get(self, request):
		weather1 = Weather.objects.all()
		serializer = WeatherSerializer(weather1, many=True)
		return Response(serializer.data)
	def post(self):
		pass
		
	