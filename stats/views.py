# stats/views.py

from django.shortcuts import render
from .models import PlayerStats

def home(request):
    return render(request, 'stats/home.html')

def search_results(request):
    query = request.GET.get('player_name')
    results = PlayerStats.objects.filter(player_name__icontains=query)
    return render(request, 'search_results.html', {'results': results})
