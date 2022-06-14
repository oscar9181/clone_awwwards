from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('AddPost/',views.addPost,name='AddPost'),
    path('site/',views.site,name='site')
    
]