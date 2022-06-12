from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('portfolio/',views.portfolio,name='portfolio')
]