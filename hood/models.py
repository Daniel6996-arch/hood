from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class NeighbourHood(models.Model):
    hood_name = models.CharField(primary_key = True, max_length = 60)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_location = models.CharField(max_length = 120)
    occupants_count = models.IntegerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    username = models.ForeignKey(User, verbose_name = 'user', related_name = 'profile', on_delete = models.CASCADE)
    id = models.IntegerField(primary_key = True, default=0)
    hood = models.ForeignKey(NeighbourHood, on_delete = models.CASCADE, default=0)   
    email = models.EmailField()

class Business(models.Model):
    business_name = models.CharField(max_length = 120, primary_key = True)
    username  = models.ForeignKey(User, on_delete = models.CASCADE)
    hood = models.ForeignKey(NeighbourHood, related_name = 'neighbourhood', on_delete = models.CASCADE, default=0)
    business_email = models.EmailField()
    uploaded_on = models.DateTimeField(auto_now_add=True)