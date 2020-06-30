import time
import random

from django.core.cache import cache

value = cache.get('key')
cache.set('key', value)

from django.shortcuts import render
from django.http import JsonResponse

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'
    context = {
        'form': SearchTicket()
    }
    return render(request, template, context)


def cities_lookup(request):
    results = []
    for word in list(item['name'] for item in City.objects.values('name').all() if item):
        if word.lower().find(request.GET.get('term').lower()) >= 0:
            results.append(word)
    return JsonResponse(results, safe=False)
