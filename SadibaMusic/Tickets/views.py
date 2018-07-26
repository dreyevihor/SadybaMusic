from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import json
from PIL import Image
import io
import base64

from .forms import *
from .tasks import *
from .models import *
from Event.models import *
# Create your views here.


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TicketsIndexView(View):
	template = 'tickets/index.html'
	def get(self, request):
		tickets = Tickets.objects.all()
		links = []
		for ticket in tickets:
			a = {
				'event': ticket.event.title,
				'href': ticket.tickets.url
			}
			links.append(a)
		return TemplateResponse(request, self.template, {'links': links})

	

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TicketsCreateView(View):
	template = 'tickets/tickets_create.html'
	def get(self, request):
		return TemplateResponse(request, self.template, {})

	def post(self, request):
		data = json.loads(request.body.decode('utf-8'))
		event = data.get('event', None)
		request.session['event_id'] = event
		hall = data.get('hall', -1)
		print(request.body, event, hall)
		if str(hall) == '-1':
			return redirect('/halls/create/')
		else:
			return redirect('/halls/fillPrice/'+str(hall))

@method_decorator(login_required(login_url='/login/'), name='dispatch')
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
		place2_props = json.loads(request.POST['place2'])
		price2_props = json.loads(request.POST['price2'])
		row2_props = json.loads(request.POST['row2'])
		rows = request.session['filled_hall']['rows']
		event_id = request.session['event_id']
		generate_tickets(rows,
			barcode_props = barcode_props,
			place_props = place_props,
			price_props = price_props,
			row_props = row_props,
			place2_props = place2_props,
			price2_props = price2_props,
			row2_props = row2_props,
			ticket_template = templ,
			event_id = event_id,
			 )


		
		
		return redirect('/tickets/index/')


