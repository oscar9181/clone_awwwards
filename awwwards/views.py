
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Site
from .serializer import SiteSerializers


def register(request):
    form=UserCreationForm()
    
    if request.method == 'POST':
         form=UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
        
    
    context ={'form':form}
    return render(request,'awwards/register.html',context)


def login(request):
    form=UserCreationForm
    context ={'form':form}
    return render(request,'awwards/login.html',context)


def home (request):
    
    return render(request,'awwards/home.html')

def portfolio (request):
    
    return render(request,'awwards/portfolio.html')

def search(request):
    return render(request,'awwards/search.html')


@api_view(['GET'])
def site(request):
    if request.method=='GET':
        my_site=Site.objects.all()
        serializer=SiteSerializers(my_site,many=True)
        
        return Response(serializer.data)
           