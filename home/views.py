import datetime

from django.db.models import Count, Sum, Value, CharField
from django.shortcuts import render

# Create your views here.
from admins.models import FeaturedProject
from projects.models import Project, Category
from projects.views.list_projects import get_project_data_for_view


def index(request):
    context = {'latest_featured_projects': get_latest_featured_projects(),
               'highest_rated_projects': get_highest_rated_projects(),
               'latest_projects': get_latest_projects(),
               'categories': get_categories_alphabetical(),
               # 'extra': get_extra_data()
               }

    print(context)
    return render(request, 'home/index.html', context=context)


def get_latest_featured_projects():
    model = FeaturedProject.objects.order_by('-date_featured')
    latest_featured_projects = get_project_data_for_view(model)
    return latest_featured_projects


def get_highest_rated_projects():
    # returns 5 projects based on rating by descending order
    model = Project.objects.order_by('-project_rating')[:5].annotate(
        num_of_backers=Count('donations'),
        amount_of_donations=Sum('donations__amount'),

    )  # the '-' is for descending
    highest_rated_projects = get_project_data_for_view(model)
    return highest_rated_projects


def get_latest_projects():
    # returns 5 latest 5 projects based on start_date
    latest_projects_model = Project.objects.order_by('-start_date')[:5]
    latest_projects_for_view = get_project_data_for_view(latest_projects_model)
    return latest_projects_for_view


def get_categories_alphabetical():
    categories = Category.objects.order_by('name')
    return categories





def calc_percentage(n1, n2):
    return (n1 / n2) * 100