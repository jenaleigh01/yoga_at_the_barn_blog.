from django.urls import path
from ratings.views import rating_view



urlpatterns = [
    path('', index_views.index, name='home'),
    path('', rating_view, name="rating-view")
]