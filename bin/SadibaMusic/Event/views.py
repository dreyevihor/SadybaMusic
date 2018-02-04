from __future__ import unicode_literals

from datetime import datetime
import pytz
from collections import OrderedDict

from django.shortcuts import render
from django.template import Template, Context, RequestContext

from Event.models import Event, Image_portfolio
# Create your views here.

def portfolio_view(request):
	template_name = '../../static/portfolio.html'
	today = datetime.utcnow().replace(tzinfo=pytz.UTC)
	events = Event.objects.filter(date__lte = today).filter(status = 'p')
	event_list = [{'%d' % i: events[i].get_context()} for i in range(events.count())]
	context = {'event_list': event_list}
	print(context)
	return render(request, 'portfolio.html', context)

def afisha_view(request):
	template_name = '../../static/events.html'
	today = datetime.utcnow().replace(tzinfo=pytz.UTC)
	events = Event.objects.filter(date__gte = today)
	event_list = [{'%d' % i: events[i].get_context()} for i in range(events.count())]
	context = {'event_list': event_list}
	print(context)
	return render(request, 'events.html', context)

def index_view(request):
	template_name = '../../static/index.html'
	context = {}
	return render(request, 'index.html', context)
