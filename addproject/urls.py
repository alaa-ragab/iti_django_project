"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import addprojects, projects, project, category, get_category_pro, tag, feature_project, ProjectView

app_name = 'project'

urlpatterns = [
    path('', projects, name='viewall'),
    path('<int:id>', project, name='viewone'),
    path('addproject', addprojects, name='add'),
    path('addcategory', category, name='addcategory'),
    path('feature', feature_project, name='feature'),
    path('addtag', tag, name='addtag'),
    path('category/<int:id>', get_category_pro, name='project_categories'),
    path('api', ProjectView.as_view()),

]
