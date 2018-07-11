from django.conf.urls import url

from . import views

urlpatterns = [
	url('index/', views.TicketsIndexView.as_view()),
	url('create/', views.TicketsCreateView.as_view()),
	url('ticketSchema/', views.TicketsSchemaView.as_view()),




]