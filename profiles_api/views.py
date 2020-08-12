from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers
from .models import UserProfile
from .permissions import UpdateOwnProfile


# Create your views here.

class UserProfileViewSet(ModelViewSet):
    """Handle creating & updating profiles"""
    """Handles all HTTP requests, via methods ie list, create,etc """
    """Authentication checks for a token in request header, if so then allows the request to go through given permission classes"""

    serializer_class = serializers.UserProfileSerializer
    # this objects manager is UserProfileManager that we created
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginAPIView(ObtainAuthToken):
    """Handle creating user authentication tokens, displaying login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES