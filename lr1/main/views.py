from django.shortcuts import render
from .models import Links


def index(request):
    if request.method == 'POST':
        obj = Links.objects.get(linkURL=request.POST["name-of-field"])
        obj.counter += 1
        obj.save()

    links = Links.objects.all()
    return render(request, 'main/index.html', {'links': links})
