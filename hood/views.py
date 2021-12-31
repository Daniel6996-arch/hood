from django.shortcuts import render, redirect
from django.views import View
from .models import NeighbourHood
from .forms import HoodForm
# Create your views here.
def index(request):
    return render(request, 'index.html') 

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