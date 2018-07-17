from rest_framework import serializers
from .models import *


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rows
        fields = ('id', 'number', 'place_from', 'place_to')

class HallSerializer(serializers.ModelSerializer):
    rows = RowSerializer(many = True)
    class Meta:
        model = Schema_hall
        fields = ('id', 'name', 'rows')


class HallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema_hall
        fields = ('id', 'name')