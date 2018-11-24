from django.contrib.auth.models import User
from .models import Trip, Media, Place
from .serializers import TripSerializer, UserSerializer, MediaSerializer, PlaceSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status

class TripViewset(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    def create(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
        	serializer.create(serializer.validated_data)
        	return Response(serializer.data, status=status.HTTP_201_CREATED)



class MediaViewset(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    def create(self, request):
        new_media = Media.objects.create(
        	url=request.data['url'],
        	size=request.data['size'],
        	type=request.data['type'],
        	trip_id=1
        )
        return Response({}, status=status.HTTP_201_CREATED)

class PlaceViewset(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    def create(self, request):
        new_media = Media.objects.create(
        	label=request.data['label'],
        	date=request.data['date'],
        	trip_id=1
        )
        return Response({}, status=status.HTTP_201_CREATED)


class UserViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()