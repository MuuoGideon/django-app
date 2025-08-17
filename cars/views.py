from django.shortcuts import render, redirect
from . models import Car
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import JsonResponse
from . serializers import CarSerializer


def car_list(request):
	cars = Car.objects.all()
	serializer = CarSerializer(cars, many=True)
	return JsonResponse({"Cars":serializer.data})




def index(request):
	return render(request, 'index.html', {})




def the_car(request):
	th_cars = Car.objects.all()
	return render(request, 'cars_list.html', {'th_cars':th_cars})