from django import forms
from django.db.models import fields
from .models import Project, ProjectsCategory, Tags


class ProjectForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all())
    class Meta:
        model = Project
        fields = ['title', 'details', 'total_target', 'start_time', 'end_time', 'featured', 'tags','category']


class TagsForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProjectsCategory
        fields = '__all__'
