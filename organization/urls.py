from django.urls import path
from organization.views import *

urlpatterns = [
    path('setup-organization', setup_organization, name='setup-organizationn'),
]
