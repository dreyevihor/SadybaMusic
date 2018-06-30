"""SadibaMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView


from rest_framework.authtoken import views as rest_framework_views


from Event.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^afisha/', afisha_view),
    url(r'^portfolio/', portfolio_view),
    url(r'^index/', index_view),
    #url(r'^test/', LoginView.as_view()),
    url(r'^api/afisha/$', AfishaList.as_view()),
    url(r'^api/portfolio/', PortfolioList.as_view()),
    url(r'^api/events/(?P<pk>[0-9]+)/$', EventDetail.as_view()),
    url(r'^api/events/$', EventList.as_view()),
    url(r'^api/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^$', RedirectView.as_view(url='index/', permanent=False), name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)