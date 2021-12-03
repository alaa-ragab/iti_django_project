from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search_all, name='project_search'),

    # path('home/category/<int:categoty_id>', views.category, name='category')
    #path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
