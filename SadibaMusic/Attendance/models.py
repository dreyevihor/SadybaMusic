from django.db import models

from Event.models import Event

# Create your models here.

class Attendance(models.Model):
	event = models.ForeignKey(Event, on_delete = models.CASCADE)
	row = models.IntegerField()
	place = models.IntegerField()
	class Meta():
		unique_together = (('event', 'row', 'place'),)
