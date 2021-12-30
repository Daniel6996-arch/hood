from django.conf.urls import url
from django.urls import path
from . import views
from .views import HoodView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', HoodView.as_view(), name='homepage'),
]