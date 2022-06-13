from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from.models import Profile,User

class NewProfileForm(forms.ModelForm):
    
    title = forms.CharField()
    date_posted = forms.DateTimeField()
    image = forms.ImageField(required=True)
    
    
    class Meta:
        Model = Profile
        fields =('title','bio','date_posted','author','image')
        


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
