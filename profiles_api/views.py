from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters

from . import serializers
from .models import UserProfile
from .permissions import UpdateOwnProfile


# Create your views here.

class UserProfileViewSet(ModelViewSet):
    """Handle creating & updating profiles"""
    """Handles all HTTP requests, via methods ie list, create,etc """

    serializer_class = serializers.UserProfileSerializer
    # this objects manager is UserProfileManager that we created
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)