from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    location = models.CharField(max_length=100)
    profile_pic=CloudinaryField('profile_pic')
    username =models.CharField(max_length=100 , null=True)
    about_me=models.TextField(null=True)
    neighbourhood_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
  
class Neighbourhood(models.Model):
    name =models.CharField(max_length=50 , null=True)
    Neighbourhood_location = models.CharField(max_length=100, null=True)
    occupants_count= models.IntegerField()
    # admin_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    health_contacts = models.CharField(max_length=20, null=True, blank=True)
    police_contacts = models.CharField(max_length=20, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    def save_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
    
# class User(models.Model):
#     first_name = models.CharField(max_length=30, null=True)
#     last_name = models.CharField(max_length=30, null=True)
#     username =models.CharField(max_length=100 , null=True)
#     email_address = models.EmailField(max_length=100, null=True)
#     password = models.CharField(max_length=100, null=True)
#     neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    


    



class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post_description = models.TextField(null=True,)
    post_image =CloudinaryField('post_image')
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()
    
    
class Business(models.Model):
    business_name = models.CharField(max_length = 100)
    business_email_address = models.EmailField(max_length=100)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    business_image = CloudinaryField('business_image' , null=True)