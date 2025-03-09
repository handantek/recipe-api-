# Create your models here.

"""
Database models

"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
# Django'nun kullanıcı yöneticisi için temel sınıf.
class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """create, save and return new user. """
        if not email:
            raise ValueError('User must have an email address. ')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        """create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email= models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # Kullanıcı aktif mi?
    is_staff = models.BooleanField(default=False) # Admin paneline erişim

    objects = UserManager()
    USERNAME_FIELD = 'email' # Giriş için email kullanılacağını belirtir.


 #model olusturma 'models django base class'
class Recipe(models.Model):
    """  Recipe object. """

    #add fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, # model silinirse tarif de silinir
    )
    title = models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    time_minutes =models.IntegerField()           #hazirlanma süresi
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link =models.CharField(max_length=255 ,blank=True)

    def __str__(self):
        return self.title



