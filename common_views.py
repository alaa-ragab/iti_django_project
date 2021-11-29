from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import ListView

from projects.models import Project
# from projects.views.list_projects import get_project_data_for_view


def render_404_page(request):
    return render(request, "crowdfunding_web_app/404/404.html")


def logout_view(request):
    logout(request)
    return render(request, "homepage/index.html")


def not_found(request):
    return render(request, "crowdfunding_web_app/404/404.html")


class SearchResultsView(ListView):
    model = Project
    template_name = 'crowdfunding_web_app/search_results.html'

    # template_name = 'projects/view_projects.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        model = Project.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        ).distinct()
        object_list = get_project_data_for_view(model)
        return object_list

        # queryset = []
        # queries = query.split(" ")
        # for query in queries:
        #     projects = Project.objects.filter(
        #         Q(title__icontains=query) |
        #         Q(category__name__icontains=query)
        #     ).distinct()
        #
        #     for project in projects:
        #         queryset.append(project)
        #
        #     return list(set(queryset))
