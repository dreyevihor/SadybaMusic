from django.conf.urls import url

from . import views

urlpatterns = [
	url('fillPrice/(?P<hall>[0-9]+)', views.FillPriceView.as_view()),
	url('create/', views.CreateHallView.as_view()),
	]