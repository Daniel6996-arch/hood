from django.shortcuts import render, redirect
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html') 

class HoodView(View):
    def get(self, request):
        hoods = Hood.objects.all().order_by('-uploaded_on')
        form = HoodForm()

        context = {
            'hood_list':hood,
            'form':form,
        }

        return render(request, 'hood.html', context) 

    def post(self, request):
        hoods = Hood.objects.all().order_by('-uploaded_on')
        hood_of_day = Hood.objects.all().order_by('-uploaded_on').first()
        form = HoodForm(request.POST, request.FILES)

        if form.is_valid():
            new_hood = form.save(commit = False)
            new_hood.author = request.user

            if 'img' in request.FILES:
                new_hood.image = request.FILES['img']

            new_hood.save()   

        context = {
            'hood_list':hoods,
            'hood_of_day':hood_of_day,
            'form':form,
        }

        return render(request, 'hood.html', context)      