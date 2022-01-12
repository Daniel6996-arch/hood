from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# Create your models here.
class NeighbourHood(models.Model):
    hood_name = models.CharField(max_length = 60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_location = models.CharField(max_length = 120)
    occupants_count = models.IntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    hood_pic = CloudinaryField()

    def save_hood(self):
        self.save() 

    def delete_hood(self):
        self.delete()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=250)
    location = models.CharField(max_length=120)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, blank=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    email =  models.CharField(max_length=60) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

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
