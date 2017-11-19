from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Template, Context, RequestContext


# Create your views here.

def portfolio(request):
	template_name = '../../static/portfolio.html'
	
	return render(request, template_name, context)
