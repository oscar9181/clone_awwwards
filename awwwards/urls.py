from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('AddPost/',views.addPost,name='AddPost'),
    path('site/',views.site,name='site'),
    path('search/',views.search,name='search'),
    # path('display',views.viewPicture,name='image'),
    
]