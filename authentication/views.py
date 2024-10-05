from django.shortcuts import render

def sign_in(request):
    return render(request, 'authentication/sign-in.html')

def sign_up(request):
    return render(request, 'authentication/sign-up.html')