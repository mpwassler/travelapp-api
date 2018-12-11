from django.contrib.auth.models import User
from .models import Trip, Place
from .serializers import TripSerializer, UserSerializer, PlaceSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from trips.permissions import IsTripOwner
from rest_framework import permissions
from rest_framework.decorators import action
from django.conf import settings
import boto3


class TripViewset(viewsets.ModelViewSet):

    serializer_class = TripSerializer
    permission_classes = (permissions.IsAuthenticated, IsTripOwner)
    queryset = Trip.objects.all()

    def get_queryset(self):
        queryset = Trip.objects.filter(user_id=self.request.user.id)
        return queryset

    # def create(self, request):
    #     serializer = TripSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.create(serializer.validated_data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)



# class MediaViewset(viewsets.ModelViewSet):
#     queryset = Media.objects.all()
#     serializer_class = MediaSerializer
#     # permission_classes = (permissions.IsAuthenticated,)




class PlaceViewset(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (permissions.IsAuthenticated)
    @action(detail=False, methods=['post'])
    def get_upload_url(self, request, pk=None, **kwargs):
        s3 = boto3.client('s3')
        fields = {"acl": "public-read"}
        conditions = [
            {"acl": "public-read"}
        ]
        post = s3.generate_presigned_post(
            Bucket=settings.AWS_BUCKET,
            Key=settings.AWS_ACCESS_KEY_ID,
            Fields=fields,
            Conditions=conditions
        )
        if True:
            return Response({'status': post})
        else:
            return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()