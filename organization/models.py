from django.db import models
from authentication.models import User
import uuid

"""
    Represents a category for an organization, including its name and description.
    The `OrganizationCategory` model stores the name and description of a category that can be associated with an organization.
"""
class OrganizationCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization_category'

    def __str__(self):
        return self.name



"""
    Represents a role that can be assigned to members of an organization, including its name and description.
    The `OrganizationRole` model stores the name and description of a role that can be associated with an `OrganizationMember`.
"""
class OrganizationRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization_role'

    def __str__(self):
        return self.name



"""
    Represents an organization, including its name, description, category, members, and creation/update timestamps.
    The `Organization` model stores the core details of an organization.
    Including a foreign key reference to the `OrganizationCategory` model and a many-to-many relationship with the `User` model through the `OrganizationMember` model.
"""
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    image =  models.ImageField(upload_to='static/uploads/', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(OrganizationCategory, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, through='OrganizationMember')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization'
    
    def __str__(self):
        return self.name



"""
    Represents a member of an organization, including their role within the organization.
    The `OrganizationMember` model links a `User` to an `Organization`, and also stores the role of the user within the organization (e.g. "admin", "member", etc.).
"""
class OrganizationMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.ForeignKey(OrganizationRole, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization_member'
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user.email} - {self.organization.name} - {self.role}"

