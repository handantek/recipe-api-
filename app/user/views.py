"""
views for the user API.

"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    )

class CreateUserView(generics.CreateAPIView):
    """create a new user in the sytem ."""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    "create a new auth token for user."
    serializer_class  = AuthTokenSerializer
    renderer_classes  = api_settings.DEFAULT_RENDERER_CLASSES

#urls.py kullaniyor
class ManageUserView(generics.RetrieveUpdateAPIView):
    """ manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes  =  [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated] # allow to do

    def get_object(self):
        """ retrieve and the authenticated user. """
        return self.request.user



