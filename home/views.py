from django.shortcuts import render
from django.views import generic
from .models import Rating

# Create your views here.


def index(request):
    """
    Renders the Homepage View
    """
    return render(request, 'home/index.html')


def rating_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'home/index.html', context)
