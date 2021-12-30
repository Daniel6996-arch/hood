from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class NeighbourHood(models.Model):
    hood_name = models.CharField(primary_key = True, max_length = 60)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_location = models.CharField(max_length = 120)
    occupants_count = models.IntergerField()
    uploaded_on = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.OneToOneField(User, primary_key = True, verbose_name = 'user', related_name = 'profile', on_delete = models.CASCADE)
    id = models.IntergerField()
    hood_id = models.ForeignKey(NeighbourHood, related_name = 'neighbourhood')   
    email = models.EmailField()

class Business(models.Model):
    business_name = models.CharField(max_length = 120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(NeighbourHood, related_name = 'neighbourhood')
    business_email = models.EmailField()