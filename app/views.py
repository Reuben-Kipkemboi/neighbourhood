from django.shortcuts import get_object_or_404, render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import ProfileUpdateForm


# Application views.
def home(request):
    posts= Post.objects.all()
    return render(request, 'index.html', {'posts':posts})


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
            return redirect ("home")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def user_profile(request):
    users= User.objects.all()
    current_user = request.user
    user_posts = Post.objects.filter(person=current_user)
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
    return render(request,'update_profile.html', {'form':form})

def user_post(request):
    if request.method=='POST':
        title=request.POST.get('title')
        post_description=request.POST.get('description')
        post_image=request.FILES.get('post_image')
        
        posts=Post(post_image=post_image,title=title,post_description=post_description)
        
        posts.save_post()
        
        return redirect('home')
    return render(request, 'post.html')


def create_hood(request):
    neighbourhood_credentials = Profile.objects.all()
    # profile = Profile.objects.get(user=admin_id)
    if request.method=='POST':
        image=request.FILES.get('image')
        describe=request.POST.get('describe')
        name =request.POST.get('name')
        neighbourhood_location=request.POST.get('location')
        occupants_count=request.POST.get('count')
        health_contacts=request.POST.get('contact')
        police_contacts=request.POST.get('police') 
        
        
        neighbourhoods=Neighbourhood(image=image,describe=describe,name=name,neighbourhood_location=neighbourhood_location,health_contacts=health_contacts,police_contacts=police_contacts,
        occupants_count=occupants_count )
        
        neighbourhoods.admin_id= request.user                      
        
        
        neighbourhoods.save_neighbourhood()
        
        return redirect('home')
    
    return render (request, 'hood.html', {'neighbourhood_credentials':neighbourhood_credentials})

def view_hoods(request):
    hoods=Neighbourhood.objects.all()
    return render(request, 'hoods.html', {'hoods':hoods})

def singlehood(request, name):
    # current_profile = request.user.profile
    neighbourhood = get_object_or_404(Neighbourhood, name=name)
    businesses = Business.objects.filter(neighbourhood_id = neighbourhood.id).all()
    posts = Post.objects.filter(neighbourhood = neighbourhood.id).all()
    return render(request, 'single.html', {'neighbourhood': neighbourhood,'businesses':businesses, 'posts':posts,})



def create_business(request):
    
    businesses=Business.objects.all()
    user = request.user
    if request.method=='POST':
        business_name =request.POST.get('name')
        business_email_address=request.POST.get('email')
        business_image=request.FILES.get('image')
        user_id=request.user
        
        
        businesses=Business(business_name=business_name,business_email_address=business_email_address,business_image=business_image,user_id=user_id )
        
        businesses.save_businesses()
        
        return redirect('home')
    return render(request, 'bus.html', {'businesses':businesses})

#User Join hood
def user_join_hood(request,id):
    neighbour = Neighbourhood.objects.get(id=id)
    current_user =request.user
    current_user.profile.neighbour = neighbour
    current_user.profile.save()
    return redirect('hoods')

#user_leave
def user_leave_hood(request,id):
    neighbour = get_object_or_404(Neighbourhood, id=id)
    current_user =request.user
    current_user.profile.neighbour = None
    current_user.profile.save()
    return redirect('hoods')





