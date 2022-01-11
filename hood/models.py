from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  

# Create your models here.
# Create your models here.
class NeighbourHood(models.Model):
    hood_name = models.CharField( primary_key = True,max_length = 60)
    hood_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_location = models.CharField(max_length = 120)
    occupants_count = models.IntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    hood_pic = CloudinaryField()

    def save_hood(self):
        self.save() 

    def delete_hood(self):
        self.delete()


class UserProfile(models.Model):
    username = models.OneToOneField(User,primary_key = True,verbose_name = 'user', related_name = 'profile', on_delete = models.CASCADE)
    #id = models.IntegerField(primary_key = True, default=0)
    hood = models.ForeignKey(NeighbourHood, on_delete = models.CASCADE, default=0)   
    email = models.EmailField()
    user_pic = CloudinaryField()

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()    

class Business(models.Model):
    business_name = models.CharField(primary_key=True, max_length = 120)
    #business_user  = models.ForeignKey(User, on_delete = models.CASCADE)
    #hood = models.ForeignKey(NeighbourHood, related_name = 'neighbourhood', on_delete = models.CASCADE, default=0)
    business_email = models.EmailField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    business_pic = CloudinaryField()

    def save_business(self):
        self.save() 

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = cls.objects.filter(business_name = search_term)
        return business     

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete  = models.CASCADE) 
    body = models.TextField(default= 'some string')  
    created_on =  models.DateTimeField(auto_now_add=True)
    image = CloudinaryField()
    def save_post(self):
        self.save() 

    def delete_post(self):
        self.delete()
