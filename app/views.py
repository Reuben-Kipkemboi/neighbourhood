from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages

# Application views.
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        return render(request,'login.html')
    return render(request, 'register.html')


def user_login(request):
    return render(request, 'login.html')


def user_logout(request):
    return render(request, 'index.html')
