"""

Tests for recipe APIs.

"""
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipe.serializers import RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """ create and return sample recipe"""
    defaults = {
        'title' : 'Sample recipe title',
        'time_minutes' : 22,
        'price' : Decimal('5.25'),
        'description' : 'Sample description',
        'link' : 'http://example.com/recipe.pdf',
        }
    defaults.update(params)
    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe




class PublicRecipeAPITests(TestCase):
    """ test unauthenticated API request."""

    def setUp(self):
        self.client = APIClient()


    def test_auth_required(self):
        """test auth is required to call API"""
        res = self.client.get(RECIPES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)



class PrivateRecipeAPITests(TestCase):
    """ test authenticated API requests."""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(

            'user@example.com',
            'testpass123',

        )
        self.client.force_authenticate(self.user)


    def test_retrive_recipes(self):
        """ test retrieving a list of recipe """
        create_recipe(user=self.user)
        create_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)
        recipes  = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)














