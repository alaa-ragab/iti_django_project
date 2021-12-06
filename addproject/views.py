import datetime
import django
from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import FeaturedProject, Project, ProjectComments, ProjectPics, ProjectComments, ReportedProjects, \
    ReportedComments, Tags, ProjectsCategory
from .form import ProjectForm, CategoryForm, TagsForm
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from django.shortcuts import render
from .serializer import ProjectSerializer
from rest_framework.response import Response


# Create your views here.
@login_required(login_url='login')
def projects(request):
    context = {}
    context['projects'] = Project.objects.all()
    context['imgs'] = ProjectPics.objects.all()

    return render(request, 'addproject/projects.html', context)


@login_required(login_url='login')
def addprojects(request, *args):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            form.save_m2m()
            # img handle
            id = Project.objects.get(project_id=myform.project_id)
            pics = request.FILES.getlist('pic')
            for pic in pics:
                Project.objects.filter(project_id = id.project_id).update(picture = pic)
                ProjectPics.objects.create(project_id=id, pic=pic)  
            return redirect('project:viewall')

    return render(request, 'addproject/projectform.html', {'form': form})


@login_required(login_url='login')
def project(request, id):
    if request.method == 'GET':
        project = Project.objects.filter(project_id=id)[0]
        comments = ProjectComments.objects.filter(project_id=id)
        imgs = ProjectPics.objects.filter(project_id = id)
        x = False
        if project.donation / project.total_target <= 0.25 :
            x = True

        project_tags = Tags.objects.filter(project = id)
        similar_projects = django.db.models.query.QuerySet
        for tag in project_tags:
            similar_projects = Project.objects.filter(tags = tag)
        return render(request, 'addproject/project.html',
        {'project': project, 'comments': comments,  'imgs' : imgs, 'x' : x , 'similar_projects' : similar_projects})

    else:
        project = Project.objects.filter(project_id=id)
        proid = Project.objects.get(project_id=id)

        if 'donate_sub' in request.POST:
            project.update(
                donation=(int(project[0].donation) + int(request.POST['donate'])))

        if 'rate_sub' in request.POST:
            project.update(
                ratings=(int(project[0].ratings) + int(request.POST['rate'])))
            project.update(raters=(int(project[0].raters) + 1))
            project.update(avg_rate=project[0].ratings / project[0].raters)

        if 'comment_sub' in request.POST:
            ProjectComments.objects.create(
                project_id=proid, comment=request.POST['comment'])

        if 'reportpro_sub' in request.POST:
            ReportedProjects.objects.create(
                project_id=proid, pro_report='Reported Project')

        if 'report_com' in request.POST:
            ReportedComments.objects.create(com_id=int(
                request.POST['com_id']), com_report='Reported Comment')

        if 'cancel' in request.POST:
            project.delete()
            return redirect(f'/project')

        return redirect(f'/project/{id}')


@login_required(login_url='login')
def category(request):
    if request.user.is_superuser :
        form = CategoryForm()
        if request.method == 'POST':
            msg = 'Done'
            form = CategoryForm(request.POST)
            try:
                form.save()
            except:
                msg = 'Category name is already exists!'    
            return render(request, 'addproject/categoryform.html', {'form': form, 'msg' : msg})
        return render(request, 'addproject/categoryform.html', {'form': form, })

    return HttpResponse('You are not Allowed!')    


@login_required(login_url='login')
def tag(request):
    if request.user.is_superuser :
        form = TagsForm()
        if request.method == 'POST':
            msg = 'Done'
            form = TagsForm(request.POST)
            try:
                form.save()
            except:
                msg = 'Tag name is already exists!'    
            return render(request, 'addproject/tagform.html', {'form': form, 'msg' : msg})
        return render(request, 'addproject/tagform.html', {'form': form, })

    return HttpResponse('You are not Allowed!')    


def get_project_data_for_view(model):
    projects_data_list = []
    for project in model:
        if isinstance(project, FeaturedProject):
            project = project.project

        projects_data_list.append(
            {
                "project_id": project.project_id,
                "project_title": project.title,
                "project_details": project.details,
                "project_user": project.user,
                "project_start_time": project.start_time,
                "project_end_time": project.end_time,
            }
        )
    return projects_data_list


def get_category_pro(request, id):
    projects = Project.objects.filter(category_id=id)
    context = {"projects": projects}
    return render(request, 'addproject/projects.html', context)



class ProjectView(APIView):
    def get(self,request):
        trainees = Project.objects.all()
        ser = ProjectSerializer(trainees, many=True)

        for i in range(len(ser.data)):
            print(ser.data[i])
        return Response(ser.data)

    def post(self,request):
        print(request.POST)
        Project.objects.create(name=request.POST['name'], address=request.POST['address'], bio=request.POST['bio'])
        return HttpResponse(status=200)