from __future__ import unicode_literals

from datetime import datetime
import pytz
from collections import OrderedDict

from django.http import Http404
from django.shortcuts import render
from django.template import Template, Context, RequestContext

from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from Event.models import Event, Image_portfolio
from Event.serializers import (EventSerializer, 
								AfishaSerializer, PortfolioSerializer)

# Create your views here.

def portfolio_view(request):
	template_name = '../../static/portfolio.html'
	events = Event.portfolio.all()
	event_list = [{'%d' % i: events[i].get_context()} for i in range(events.count())]
	context = {'event_list': event_list}
	print(context)
	return render(request, 'portfolio.html', context)

def afisha_view(request):
	template_name = '../../static/events.html'
	events = Event.afisha.all()
	event_list = [{'%d' % i: events[i].get_context()} for i in range(events.count())]
	context = {'event_list': event_list}
	print(context)
	return render(request, 'events.html', context)

def index_view(request):
	template_name = '../../static/index.html'
	context = {}
	return render(request, 'index.html', context)

#api views

class AfishaList(generics.ListAPIView):
	queryset = Event.afisha.all()
	serializer_class = AfishaSerializer


class PortfolioList(generics.ListAPIView):
	queryset = Event.portfolio.all()
	serializer_class = PortfolioSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = (IsAdminUser, )

class EventList(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
