from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('the_car/', views.the_car, name='the-car'),
	path('car_list/', views.car_list, name='car-list')
]