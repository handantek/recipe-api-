"""
views for the user API.

"""
from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create a new user in the sytem ."""
    serializer_class = UserSerializer
