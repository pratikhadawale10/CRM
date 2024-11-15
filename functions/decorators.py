from django.shortcuts import redirect
from functools import wraps
from authentication.models import *



def login_required_redirect(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect('/auth/sign-in')
    return _wrapped_view



def redirect_if_authenticated(redirect_url):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator



def redirect_if_not_personal_details_completed(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_journey, created = UserJourney.objects.get_or_create(user=request.user)
            
            if not user_journey.profile_details:
                return redirect('/auth/personal-details')

            return view_func(request, *args, **kwargs)
        return redirect('/auth/sign-in')
    return _wrapped_view



def redirect_if_not_user_journey_completed(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_journey, created = UserJourney.objects.get_or_create(user=request.user)
            
            if not user_journey.profile_details:
                return redirect('/auth/personal-details')
            
            elif not user_journey.organization_setup:
                return redirect('/organization/setup-organization')

            return view_func(request, *args, **kwargs)
        return redirect('/auth/sign-in')
    return _wrapped_view



def redirect_if_already_setup_organization(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_journey, created = UserJourney.objects.get_or_create(user=request.user)
            if user_journey.organization_setup:
                return redirect('/home')
        else:
            return redirect('/auth/sign-in')
        return view_func(request, *args, **kwargs)
    return _wrapped_view



def redirect_if_already_profile_setup(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            user_journey, created = UserJourney.objects.get_or_create(user=request.user)
            if user_journey.profile_details:
                return redirect('/home')
        else:
            return redirect('/auth/sign-in')
        return view_func(request, *args, **kwargs)
    return _wrapped_view