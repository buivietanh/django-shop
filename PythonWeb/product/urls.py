from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.all, name='home_product'),
    path('all/', views.all, name='all_product'),
    re_path('(?P<slug>.*)', views.single, name='single_product'),
    
    #path('<slug>', views.single, name='single_product'),
]