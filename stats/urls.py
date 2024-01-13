# stats/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # Root URL for 'stats' app
    path('home/', views.home, name='home'),  # '/home' URL for 'stats' app
    path('search/', views.search_results, name='search_results'),
]
