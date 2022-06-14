from urllib import response
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Site,Profile
from .serializer import SiteSerializers
from urllib import request
import json
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login
def register(request):
    form=CreateUserForm()
    
    if request.method == 'POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
             form.save()
             
        

    context ={'form':form}
    return render(request,'awwards/register.html',context)


def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
   
    return render(request,'awwards/login.html')


def home (req):
    url='http://127.0.0.1:8000/site/'
    response=request.urlopen(url)
    results=response.read()
    data=json.loads(results)
    
    
    return render(req,'awwards/home.html',{'data':data})

def profile(req):
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     image = request.FILES['image']
    #     bio = request.POST.get('bio')
        
        
        
        # my_profile = Profile.objects.all()
        return render(req, 'awwards/profile.html')
        
        
        

def search(request):
    
    
    return render(request,'awwards/search.html')


@api_view(['GET'])
def site(request):
    if request.method=='GET':
        my_site=Site.objects.all()
        serializer=SiteSerializers(my_site,many=True)
        
        return Response(serializer.data)
    
    