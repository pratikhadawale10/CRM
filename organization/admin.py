from django.contrib import admin
from organization.models import *

admin.site.register(Organization)
admin.site.register(OrganizationCategory)
admin.site.register(OrganizationRole)
admin.site.register(OrganizationMember)