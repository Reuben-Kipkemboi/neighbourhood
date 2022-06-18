from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

    
    
class Neighbourhood(models.Model):
    name =models.CharField(max_length=100 , null=True)
    Neighbourhood_location = models.CharField(max_length=100, null=True)
    occupants_count= models.IntegerField()
    # admin_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
class User(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    username =models.CharField(max_length=100 , null=True)
    email_address = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    location = models.CharField(max_length=100)
    profile_pic=CloudinaryField('profile_pic')
    username =models.CharField(max_length=100 , null=True)
    about_me=models.TextField(null=True)
    neighbourhood_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    



class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post_description = models.TextField(null=True,)
    post_image =CloudinaryField('post_image')
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    
class Business(models.Model):
    business_name = models.CharField(max_length = 100)
    business_email_address = models.EmailField(max_length=100)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    Neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)