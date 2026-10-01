from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estoque/', views.estoque, name='estoque'),
    path('quick-search/', views.quick_search, name='quick_search'),
    # ...
]