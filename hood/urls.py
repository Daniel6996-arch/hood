from django.conf.urls import url
from django.urls import path
from . import views
from .views import HoodView, BusinessView, ProfileView, ProfileEditView, HoodFormView, PostView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('homepage/', HoodView.as_view(), name='homepage'),
    path('hood/business/', BusinessView.as_view(), name='business'),
    url('^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name = 'profile'),
    url('^profile/edit/(?P<pk>\d+)/$', ProfileEditView.as_view(), name = 'profile-edit'),
    url('^hood/form/', HoodFormView.as_view(), name='hood-form'),
    url('posts', PostView.as_view(), name='posts'),
]