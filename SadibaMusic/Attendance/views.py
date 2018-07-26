from django.shortcuts import render, redirect
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from django.views import View
from django.db.models import Count
from django.template.response import TemplateResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import *
from .serializers import *
# Create your views here.

class AttendanceCreateAPI(CreateAPIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = (IsAdminUser, )

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AttendanceListView(View):
    template = 'tickets/statistic.html'
    def get(self, request):
        attend = Attendance.objects.values('event__title', 'event__id').annotate(entries=Count('*'))
        return TemplateResponse(request, self.template, {'attend': attend})


@login_required(login_url='/login/')
def clear_pk_view(request, pk):
    Attendance.objects.filter(event__id = pk).delete()
    return redirect('/attendance/stat/')