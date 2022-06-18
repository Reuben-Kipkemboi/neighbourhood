from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Application views.
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email_address = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create(first_name=first_name,last_name=last_name,username=username,email_address=email_address,password=password1)
        
        new_user.save()
        return redirect ("login") 
    return render(request, 'register.html')


def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ('home')
    return render(request, 'login.html')


def user_logout(request):
    return render(request, 'index.html')
