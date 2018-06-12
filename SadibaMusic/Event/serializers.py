# -*- coding: utf-8 -*- 

from rest_framework import serializers
from Event.models import Event, Image_portfolio



class PhoneSerializer(serializers.Serializer):
	phone = serializers.CharField(max_length=30)


class AfishaSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	images = serializers.CharField(source='get_image', allow_null=True)
	date = serializers.DateTimeField()
	price = serializers.IntegerField()
	min_price = serializers.IntegerField()
	max_price = serializers.IntegerField()
	place = serializers.CharField(max_length=30)
	title = serializers.CharField(max_length=30)
	text = serializers.CharField(max_length=450, source='get_text')
	phones_of_managers = PhoneSerializer(many=True, allow_null=True)





class PortfolioSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	images = serializers.ListField(child=serializers.CharField(), source='get_image')
	date = serializers.DateTimeField()
	price = serializers.IntegerField()
	min_price = serializers.IntegerField()
	max_price = serializers.IntegerField()
	place = serializers.CharField(max_length=30)
	title = serializers.CharField(max_length=30)
	text = serializers.CharField(max_length=450, source='get_text')

class ImagePortfolioSerializer(serializers.Serializer):
	image = serializers.ImageField(use_url='media/')

class EventSerializer(serializers.ModelSerializer):
	portfolio_image = ImagePortfolioSerializer(many=True)
	class Meta:
		model = Event
		fields = ('id', 'title', 'afisha_image', 'portfolio_text',
		 'afisha_text', 'place', 'status', 'price', 'min_price', 
		 'max_price', 'date', 'portfolio_image')

	def create(self, validated_data):
		portfolio_image = validated_data.pop('portfolio_image')
		event = Event.objects.create(**validated_data)
		for portfolio_image in portfolio_image:
			Image_portfolio.objects.create(event=event, **portfolio_image)
		return event

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.afisha_image = validated_data.get('afisha_image', instance.afisha_image)
		instance.portfolio_text = validated_data.get('portfolio_text', instance.portfolio_text)
		instance.afisha_text = validated_data.get('afisha_text', instance.afisha_text)
		instance.place = validated_data.get('place', instance.place)
		instance.status = validated_data.get('status', instance.status)
		instance.price = validated_data.get('price', instance.price)
		instance.min_price = validated_data.get('min_price', instance.min_price)
		instance.max_price = validated_data.get('max_price', instance.max_price)
		instance.date = validated_data.get('date', instance.date)
		instance.save()
		for img in validated_data.get('portfolio_image'):
			Image_portfolio.objects.create(event=instance, image=image)
		return instance
