from django.db import models


class Car(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	stock = models.IntegerField()

	def __str__(self):
		return self.name





