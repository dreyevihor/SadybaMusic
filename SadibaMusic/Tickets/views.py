from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse


import json
from PIL import Image
import io
import base64

from .forms import *
from .tasks import *
# Create your views here.



class TicketsIndexView(View):
	template = 'tickets/index.html'
	def get(self, request):
		return TemplateResponse(request, self.template, {})


class TicketsCreateView(View):
	template = 'tickets/tickets_create.html'
	def get(self, request):
		return TemplateResponse(request, self.template, {})


class TicketsSchemaView(View):
	template = 'tickets/make_ticket.html'

	def get(self, request):
		return TemplateResponse(request, self.template, {})
	def post(self, request):
		b64 = request.POST['image'].split('base64,')[-1]
		bt = base64.b64decode(b64)
		templ = Image.open(io.BytesIO(bt))
		barcode_props = json.loads(request.POST['barcode'])
		place_props = json.loads(request.POST['place'])
		price_props = json.loads(request.POST['price'])
		row_props = json.loads(request.POST['row'])
		rows = request.session['filled_hall']['rows']
		make_ticket(
			price_val=10,
			row_val=15,
			place_val=20,
			event_id = 4,
			barcode_props = barcode_props,
			place_props = place_props,
			price_props = price_props,
			row_props = row_props,
			ticket_template = templ
		).show()


		
		
		return TemplateResponse(request, self.template, {})


