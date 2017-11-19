from django.db import models
import datetime

# Create your models here.

STATUS_CHOICES = (
	('e', 'Event'),
	('p', 'Portfolio'),
	('w', 'Wait')
	)

class Event(models.Model):
	class Meta():
		db_table = 'Event'
	title = models.TextField(null = True, max_length = 30)
	portfolio_image = models.ImageField(null = True,)
	afisha_text = models.TextField(null = True, max_length = 450)
	portfolio_text = models.TextField(null = True, max_length = 250)
	date = models.DateTimeField(null = True)
	price = models.IntegerField(null = True)
	min_price = models.IntegerField(null = True)
	max_price = models.IntegerField(null = True)
	place = models.CharField(null = True, max_length = 30)
	status = models.CharField(null = True, default = 'e', max_length = 1, choices = STATUS_CHOICES)

	def get_price(self):
		if self.price == None:
			return {
					'min_price': self.min_price,
					'max_price': self.max_price
					}
		if self.price != None:
			return {
					'price' : self.price
				   }
		else:
			raise BaseException('Price dont exist')

"""	def get_text():
		if date <:
			pass
"""



class Image_afisha(models.Model):
	class Meta():
		db_table = 'Image'
	image = models.ImageField(null = True)
	event = models.ForeignKey(Event, null = True)