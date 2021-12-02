from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
    #path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
