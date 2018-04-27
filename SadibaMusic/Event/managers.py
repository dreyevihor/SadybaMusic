from __future__ import unicode_literals

from datetime import datetime
import pytz

from django.db import models


class AfishaManager(models.Manager):
	def get_queryset(self):
		return super(models.Manager, self).get_queryset().filter(date__gte=datetime.utcnow().replace(tzinfo=pytz.UTC)).filter(status = 'e')


class PortfolioManager(models.Manager):
	def get_queryset(self):
		return super(models.Manager, self).get_queryset().filter(date__lte=datetime.utcnow().replace(tzinfo=pytz.UTC)).filter(status = 'p')