from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from authentication.models import User
from functions.decorators import *

@redirect_if_authenticated(redirect_url='/home')
def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'authentication/sign-in.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)



@redirect_if_authenticated(redirect_url='/home')
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'authentication/sign-up.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match'}, status=400)
        
        if User.objects.filter(username=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'}, status=400)
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        user = authenticate(request, username=email, password=password)
        login(request, user)
        return JsonResponse({'status': 'success'})



@login_required_redirect
def personal_details(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'authentication/personal-details.html')
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mobile = request.POST.get('mobile')
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.mobile = mobile
            user.save()
            return redirect('/home')
    else:
        return redirect('/auth/sign-in')
        


def sign_out(request):
    logout(request)
    return redirect('/auth/sign-in')



def index(request):
    return render(request, 'index.html')



def home(request):
    context = {'title':'Home'}
    return render(request, 'home.html', context)