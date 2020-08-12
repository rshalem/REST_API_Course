from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Custom Manager class tbu in command line while creating new users, as below userprofile class expects email field & not the default username field"""

    def create_user(self, email, name, password=None):
        """Create a new user profile obj"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)

        # create a new user model obj for which this Manager is defined for
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new user superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    # instead of username field use email field as default
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of User"""
        return self.name

    def __str__(self):
        return self.email
    