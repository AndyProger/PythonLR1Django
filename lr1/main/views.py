from django.shortcuts import render
from .models import Links


def index(request):
    links = Links.objects.all()
    return render(request, 'main/index.html', {'links': links})
