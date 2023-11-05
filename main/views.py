from django.shortcuts import render
from .models import Band


def main_page(request):
    data = Band.objects.all()
    return render(request, 'main/index_main.html', {'data': data})


def about_page(request, slug):
    data = Band.objects.get(slug=slug)
    return render(request, 'main/index_about.html', {'data': data})
