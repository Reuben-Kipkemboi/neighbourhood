from django.shortcuts import render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import check_password


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
        
        # user = User.objects.get(username=username)
        user = authenticate (username=username,password=password)
        print("user is -->",user)
        # if check_password(password, user.password):
        #     if user.is_active:
        #         login(request, user)
        #         return redirect ('home')
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ('home')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def user_profile(request):
    users= User.objects.all()
    current_user = request.user
    user_posts = Post.objects.filter(user=current_user)
    print(user_posts)
    
    return render (request, 'profile.html', {'users':users, 'user_posts':user_posts})

def update_profile(request):
    
    if request.method == 'POST':
        userprofileform = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if  userprofileform.is_valid():
            userprofileform.save()
            return redirect(to='profile')
    else:
        form=ProfileUpdateForm(instance =request.user.profile)
    return render(request,'update_profile.html',{'form':form})

# def user_post(request):
#     if request.method=='POST':
#         title=request.POST.get('title')
#         post_description=request.POST.get('description')
#         post_image=request.FILES.get('post_image')
        
#         posts=Post(post_image=post_image,title=title,post_description=post_description)
        
#         posts.save_post()
        
#         return redirect('home')
#     return render(request, 'post.html')
