from django.contrib import admin
from . models import Car


class CarAdmin(admin.ModelAdmin):
	list_display = ('name','price','stock')
	fields = (('name','price'), 'stock')
	search_fields = ('name',)
	list_filter = ('price',)
	ordering = ('name',)


admin.site.register(Car, CarAdmin)