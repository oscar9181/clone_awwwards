from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from.models import User

# class NewProfileForm(forms.ModelForm):
    
#     title = forms.CharField()
#     bio = forms.Textarea()
#     picture = forms.ImageField(required=True)
    
    
#     class Meta:
#         Model = Profile
#         fields =('picture','bio','author')
        


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
