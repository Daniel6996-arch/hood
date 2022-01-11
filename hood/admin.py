from django.contrib import admin
from .models import NeighbourHood,Business, UserProfile

# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(UserProfile)