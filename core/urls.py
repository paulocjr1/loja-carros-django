from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('quick-search/', views.quick_search, name='quick_search'),
    # ...
]