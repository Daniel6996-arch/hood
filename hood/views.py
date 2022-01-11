from django.shortcuts import render, redirect
from django.views import View
from .models import NeighbourHood, Business, UserProfile, Posts
from .forms import HoodForm, BusinessForm, PostForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.
def index(request):
    return render(request, 'index.html') 

def contact(request):
    return render(request, 'contact.html')     
    
class HoodFormView(View):
    def get(self, request):
        hood = NeighbourHood.objects.all().order_by('-uploaded_on')
        form = HoodForm()

        context = {
            'hood':hood,
            'form':form,
        }

        return render(request, 'hood_form.html', context) 

    def post(self, request):
        hood = NeighbourHood.objects.all().order_by('-uploaded_on')
        form = HoodForm(request.POST, request.FILES)

        if form.is_valid():
            new_hood = form.save(commit = False)
            new_hood.author = request.user

            if 'img' in request.FILES:
                new_hood.image = request.FILES['img']

            new_hood.save()   

        context = {
            'hood':hood,
            'form':form,
        }

        return render(request, 'hood_form.html', context)  

class HoodView(View):
    def get(self, request):
        hood = NeighbourHood.objects.all().order_by('-uploaded_on')
        form = HoodForm()

        context = {
            'hood':hood,
            'form':form,
        }

        return render(request, 'hood.html', context) 

    def post(self, request):
        hood = NeighbourHood.objects.all().order_by('-uploaded_on')
        form = HoodForm(request.POST, request.FILES)

        if form.is_valid():
            new_hood = form.save(commit = False)
            new_hood.author = request.user

            if 'img' in request.FILES:
                new_hood.image = request.FILES['img']

            new_hood.save()   

        context = {
            'hood':hood,
            'hood_of_day':hood_of_day,
            'form':form,
        }

        return render(request, 'hood.html', context)  

class BusinessView(View):
    def get(self, request):
        business = Business.objects.all().order_by('-uploaded_on')
        form = BusinessForm()

        context = {
            'business':business,
            'form':form,
        }

        return render(request, 'business.html', context) 

    def post(self, request):
        business = NeighbourHood.objects.all().order_by('-uploaded_on')
        form = BusinessForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = User.objects.get(username=self.request.user)
            new_business = form.save(commit = False)
            new_business.user = request.user

            if 'img' in request.FILES:
                new_business.image = request.FILES['img']

            new_business.save()   

        context = {
            'business':business,
            'form':form,
        }

        return render(request, 'business.html', context)  

class ProfileView(View):
    def get(self, request, pk):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        hood = NeighbourHood.objects.filter(hood_admin = profile).order_by('-uploaded_on')   

        context = {
            'user':user,
            'profile':profile,
            'hood':hood,
        }        

        return render(request, 'profile.html', context)     

class ProfileEditView(UpdateView):
    model = UserProfile
    fields = ['full_name', 'bio']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk':pk})

    def test_func(self):
        profile = self.get_object()         

class PostView(View):
    def get(self, request):
        posts = Posts.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
            'post':posts,
            'form':form,
        }

        return render(request, 'post.html', context) 

    def post(self, request):
        posts = Posts.objects.all().order_by('-created_on')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = User.objects.get(username=self.request.user)
            new_post = form.save(commit = False)
            new_post.author = request.user

            if 'img' in request.FILES:
                new_post.image = request.FILES['img']

            new_post.save()   

        context = {
            'posts':posts,
            'form':form,
        }

        return render(request, 'post.html', context)                 

def search(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"users":searched_users})

    else:
        return render(request, 'search.html', {"message":message})        