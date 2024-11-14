from django.contrib import admin
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('sign-out', sign_out, name='sign-out'),
    path('personal-details', personal_details, name='personal-details'),
]
