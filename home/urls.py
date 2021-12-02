from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.index, name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
