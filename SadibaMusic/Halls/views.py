from django.views import View
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from . import forms
from Halls.models import *
from .serializers import *



from rest_framework import generics
from rest_framework.permissions import IsAdminUser



import json

# Create your views here.
class CreateHallView(View):
	template = 'tickets/make_hall.html'
	form_class = forms.RowForm
	def get(self, request):
		return TemplateResponse(request, self.template, {})
	def post(self, request):
		data = json.loads(request.body.decode('utf-8'))
		hall, created = Schema_hall.objects.get_or_create(name = data['title'])
		for row_instance in data['rows']:
			form = self.form_class(row_instance)
			if form.is_valid():
				row = form.cleaned_data
				for i in range(row['row_from'], row['row_to']+1):
					obj, created = Rows.objects.update_or_create(
						hall = hall, number = i,
						defaults = {'hall': hall, 'number': i,
						'place_from': row['place_from'],
						'place_to': row['place_to']})
		return redirect('/halls/fillPrice/' + str(hall.id))


class FillPriceView(View):
	template = 'tickets/hall_fill.html'
	def get(self, request, hall):
		return render(request, self.template, {})
	def post(self, request, hall):
		filled_hall = json.loads(request.body.decode('utf-8'))
		request.session['filled_hall'] = filled_hall
		return redirect('/tickets/ticketSchema/')

class HallsDetail(generics.RetrieveAPIView):
	serializer_class = HallSerializer
	queryset = Schema_hall.objects.all()
	permission_class = [IsAdminUser]

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

class HallsList(generics.ListAPIView):
	serializer_class = HallListSerializer
	permission_class = [IsAdminUser]
	queryset = Schema_hall.objects.all()
