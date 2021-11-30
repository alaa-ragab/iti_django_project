from django import forms
from django.db.models import fields
from .models import Project, ProjectsCategory

class ProjectForm(forms.ModelForm): 
        class Meta :
            model = Project
            fields = ['title',  'details', 'total_target', 'start_time', 'end_time', 'tag', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProjectsCategory
        fields = '__all__'

