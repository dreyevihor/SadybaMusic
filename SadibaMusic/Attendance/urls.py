from django.conf.urls import url

from . import views

urlpatterns = [
	url('stat/', views.AttendanceListView.as_view()), 
	url('clear/(?P<pk>[0-9]+)', views.clear_pk_view),
	]