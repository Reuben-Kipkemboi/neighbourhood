from pydoc import describe
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# models here.

class Neighbourhood(models.Model):
    image=CloudinaryField('image', null=True)
    describe = models.TextField(null=True)
    name =models.CharField(max_length=50 , null=True)
    neighbourhood_location = models.CharField(max_length=100, null=True)
    occupants_count= models.IntegerField(default=0)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    health_contacts = models.CharField(max_length=20, null=True, blank=True)
    police_contacts = models.CharField(max_length=20, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
        
    def update_neighbourhood(self):
        self.update()
        
#profile
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    location = models.CharField(max_length=100)
    profile_pic=CloudinaryField('profile_pic')
    username =models.CharField(max_length=100 , null=True)
    about_me=models.TextField(null=True)
    neighbour = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank=True , related_name='jirani')
    
    
    def __str__(self):
        return self.user.username
    
    def save_Profile(self):
        self.save()
        
    def delete_Profile(self):
        self.delete()
        
    def update_Profile(self):
        self.update()
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post_description = models.TextField(null=True,)
    post_image =CloudinaryField('post_image')
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    def update_post(self):
        self.update()
    
    
class Business(models.Model):
    business_name = models.CharField(max_length = 100)
    business_email_address = models.EmailField(max_length=100)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank=True)
    business_image = CloudinaryField('business_image' , null=True)
    
    def __str__(self):
        return self.business_name
    
    
    def save_businesses(self):
        self.save()
        
        
    def delete_businesses(self):
        self.delete()
        
    def update_businesses(self):
        self.update()
        
     
    @classmethod
    def get_hood_business(cls,id):
        business = Business.objects.filter(neighbourhood_id__pk = id)
        return business