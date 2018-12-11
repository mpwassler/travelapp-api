from rest_framework import serializers
from .models import Trip, Place
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point

class TripSerializer(serializers.ModelSerializer):
	user = serializers.HiddenField(
    	default=serializers.CurrentUserDefault()
	)
	class Meta:
		model = Trip
		fields = ( 'id', 'title', 'description', 'user', 'places', 'user_id')
		depth = 1

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email')
		depth = 1

# class MediaSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Media
# 		fields = ('url', 'size', 'type', 'entity', 'place')
# 		depth = 1

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ('label', 'date', 'location')