from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
    
    path('portfolio/',views.portfolio,name='portfolio'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('search/',views.search),
    path('site/',views.site,name='site')
    
]