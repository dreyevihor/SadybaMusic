from __future__ import unicode_literals

from datetime import datetime
import pytz
from collections import OrderedDict
from dateparser import parse

from django_filters.rest_framework import DjangoFilterBackend


from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import Template, Context, RequestContext

from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import LimitOffsetPagination

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



def sitemap_view(request):
	return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')

#api views

class AfishaList(generics.ListAPIView):
	serializer_class = AfishaSerializer
	def get_queryset(self):
		queryset = Event.afisha.all()
		place = self.request.query_params.get('place', '')
		min_date = self.request.query_params.get('min_date', '')
		max_date = self.request.query_params.get('max_date', '')
		if place is not '':
			queryset = queryset.filter(place=place)
		if min_date is not '' and parse(min_date) is not None:
			queryset = queryset.filter(date__gte = parse(min_date).replace(tzinfo=pytz.UTC))
		if max_date is not '' and parse(max_date) is not None:
			queryset = queryset.filter(date__lte = parse(max_date).replace(tzinfo=pytz.UTC))
		return queryset


class PortfolioList(generics.ListAPIView):
	queryset = Event.portfolio.all()
	serializer_class = PortfolioSerializer
	pagination_class = LimitOffsetPagination


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = (IsAdminUser, )

class EventList(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
