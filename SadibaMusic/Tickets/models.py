from django.db import models

from Event.models import Event

# Create your models here.

class Tickets(models.Model):
	tickets = models.FileField(upload_to = 'tickets/')
	event = models.ForeignKey(Event, on_delete = models.CASCADE)


