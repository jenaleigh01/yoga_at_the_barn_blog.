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
    queryset = Rating.objects.all()
    template_name = "home/index.html"
    
    return render(
        request, 
        "home/index.html",
    {
       "rating": rating, 
    }

)
    
