from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser


from .models import *
from .serializers import *
# Create your views here.

class AttendanceCreateAPI(CreateAPIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = (IsAdminUser, )