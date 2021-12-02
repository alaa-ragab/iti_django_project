from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from addproject.models import Project, ProjectPics
from addproject.views import get_project_data_for_view, projects

# # Create your views here.
app_name = 'home'


def index(request):
    context = {
        'latest_featured': get_latest_featured_projects(),
        'get_latest_projects': get_latest_projects(),
    }

    return render(request, 'home/index.html', context)


def get_latest_featured_projects():
    model = Project.objects.order_by('-start_time')
    latest_featured_projects = get_project_data_for_view(model)
    return latest_featured_projects


def get_latest_projects():
    # returns 5 latest 5 projects based on start_date
    latest_projects_model = Project.objects.order_by('-start_time')[:5]
    latest_projects_for_view = get_project_data_for_view(latest_projects_model)
    return latest_projects_for_view


def showCategoryProjects(request, cat_id):
    c = get_object_or_404('Categories', pk=cat_id)
    category_projects = c.projects_set.all()
    project_pics2 = {}

    for p in category_projects:
        project_pics = ProjectPics.objects.filter(project=p.id)
        project_pics2[p.id] = project_pics[0]
    context = {
        'category_name': c.title,
        'c': c,
        'category_projects': category_projects,
        'pics':  project_pics2
    }
    return render(request, "viewCategory.html", context)


class SearchResultsView(ListView):
    model = Project
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        model = Project.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        ).distinct()
        object_list = projects(model)
        return object_list
