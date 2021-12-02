import django_filters
from addproject.models import Project


class CompanyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['title', 'tag']
