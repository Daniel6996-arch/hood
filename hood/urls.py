from django.conf.urls import url
from django.urls import path
from . import views
from .views import HoodView, BusinessView, ProfileView, ProfileEditView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', HoodView.as_view(), name='homepage'),
    path('hood/business/', BusinessView.as_view(), name='business'),
    url('^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name = 'profile'),
    url('^profile/edit/(?P<pk>\d+)/$', ProfileEditView.as_view(), name = 'profile-edit'),
]