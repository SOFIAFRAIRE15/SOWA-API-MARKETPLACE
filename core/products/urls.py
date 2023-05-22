#from django.contrib import admin 
from django.urls import path
from .views import ProductView


urlpatterns = [
    #path('admin/',admin.site.urls ),
    path('', ProductView.as_view(), name = 'product'),
]