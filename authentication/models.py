from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

"""
    Defines the custom User model for the application, which extends the AbstractUser model provided by Django.
    
    The custom User model includes the following additional fields:
    - email (EmailField): The user's email address, which must be unique.
    - first_name (CharField): The user's first name, with a maximum length of 30 characters.
    - last_name (CharField): The user's last name, with a maximum length of 30 characters.
    - mobile (CharField): The user's mobile phone number, with a maximum length of 15 characters.
"""
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image =  models.ImageField(upload_to='static/uploads/', null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
    

"""
    Defines a model for tracking the progress of a user's journey through the application.

    The `UserJourney` model has the following fields:
    - `id`: A unique UUID identifier for the user journey.
    - `user`: A one-to-one relationship with the `User` model, representing the user associated with this journey.
    - `profile_details`: A boolean flag indicating whether the user has completed the profile details step.
    - `organization_setup`: A boolean flag indicating whether the user has completed the organization setup step.
    - `created_at`: The date and time when the user journey was created.
    - `updated_at`: The date and time when the user journey was last updated.
"""
class UserJourney(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_details = models.BooleanField(default=False)
    organization_setup = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_journey'

    def __str__(self):
        return self.user.email