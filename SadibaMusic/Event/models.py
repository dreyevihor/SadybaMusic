from django.db import models




from datetime import datetime
import pytz


from Event.managers import AfishaManager, PortfolioManager
# Create your models here.

STATUS_CHOICES = (
	('e', 'Event'),
	('p', 'Portfolio'),
	('w', 'Wait')
	)

	
class Event(models.Model):
	class Meta():
		db_table = 'Event'
		ordering = ('-date',)
	title = models.CharField(null = True, blank = True, max_length = 30)
	afisha_image = models.ImageField(null = True, blank = True, upload_to= 'media/')
	afisha_text = models.TextField(null = True, blank = True, max_length = 450)
	portfolio_text = models.TextField(null = True, blank = True, max_length = 250)
	date = models.DateTimeField(null = True, blank = True)
	price = models.IntegerField(null = True, blank = True)
	min_price = models.IntegerField(null = True, blank = True)
	max_price = models.IntegerField(null = True, blank = True)
	place = models.CharField(null = True, blank = True, max_length = 30)
	status = models.CharField(null = True, blank = True, default = 'e', max_length = 1, choices = STATUS_CHOICES)
	objects  = models.Manager()
	afisha = AfishaManager()
	portfolio = PortfolioManager()


	def get_price(self):
		if self.price == None:
			return  {
					'min_price':	self.min_price, 
					'max_price':	self.max_price
					  }
		if self.price != None:
			return {'price': self.price}
		else:
			raise BaseException('Price dont exist')

	def get_text(self):
		today = datetime.utcnow().replace(tzinfo=pytz.UTC)
		if self.date < today:
			return self.portfolio_text
		else:
			return self.afisha_text

	def get_image(self):
		today = datetime.utcnow().replace(tzinfo=pytz.UTC)
		if self.date < today:
			images_obj = Image_portfolio.objects.filter(event = self)
			images = [obj.image.url for obj in images_obj]
			return  images
					
		else:
			return self.afisha_image.url


	def get_context(self):
		dict = {'title' : self.title,
				'date' : self.date,
				'place' : self.place
				}
		dict.update({'text': self.get_text()})
		dict.update({'images': self.get_image()})
		dict.update(self.get_price())
		return dict





class Image_portfolio(models.Model):
	class Meta():
		db_table = 'Image'
	image = models.ImageField(null = True, upload_to= 'media/')
	event = models.ForeignKey(Event, related_name = 'portfolio_image', on_delete = models.CASCADE, null = True)


class Phones(models.Model):
	phone = models.CharField(max_length = 30)
	event = models.ForeignKey(Event, related_name = 'phones_of_managers', on_delete = models.CASCADE)