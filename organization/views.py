from django.shortcuts import render
from functions.decorators import *
from organization.models import *

@login_required_redirect
@redirect_if_not_personal_details_completed
@redirect_if_already_setup_organization
def setup_organization(request):
    if request.method == 'GET':
        contxt = {'organization_categories': OrganizationCategory.objects.all()}
        return render(request, 'organization/setup-organization.html', contxt)
    
    elif request.method == 'POST':
        type = request.POST.get('type')
        if type == 'create_organization':
            organization_name = request.POST.get('organization_name')
            organization_category_id = request.POST.get('organization_category_id')
            organization_category = OrganizationCategory.objects.get(id=organization_category_id)
            organization_description = request.POST.get('organization_description')

            organization = Organization.objects.create(
                name=organization_name,
                category=organization_category,
                description=organization_description,
                created_by=request.user
            )

            role = OrganizationRole.objects.get(name='Admin')

            member = OrganizationMember.objects.create(
                organization=organization,
                user=request.user,
                role=role
            )

            journey = UserJourney.objects.get(user = request.user)
            journey.organization_setup = True
            journey.save()

            return redirect('/home')
    
        elif type == 'invite_code':
            pass
