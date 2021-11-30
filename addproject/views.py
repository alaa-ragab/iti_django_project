from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Project, ProjectComments, ProjectPics, ProjectComments, ReportedProjects, ReportedComments
from .form import ProjectForm

# Create your views here.
def projects(request):
    context = {}
    context['projects'] = Project.objects.all()    
    return render(request, 'addproject/projects.html', context)
    


def addprojects(request, *args):
    if request.method == 'GET':
        form = ProjectForm()
        return render(request, 'addproject/projectform.html', {'form' : form})
    else:    
        form = ProjectForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            return HttpResponse('failed to save info please try again')



def project(request, *args):
    if request.method == 'GET':
        project = Project.objects.filter(project_id = args[0])[0]
        comments = ProjectComments.objects.filter(project_id = args[0])
        return render(request, 'addproject/project.html', {'project' : project,'comments' : comments})

    else:
        project = Project.objects.filter(project_id = args[0])
        proid = Project.objects.get(project_id=args[0])


        if 'donate_sub' in request.POST :
            project.update(donation= (int(project[0].donation) + int(request.POST['donate'])))

        if 'rate_sub' in request.POST :
            project.update(ratings= (int(project[0].ratings) + int(request.POST['rate'])))
            project.update(raters= (int(project[0].raters) + 1))
            project.update(avg_rate = project[0].ratings / project[0].raters)
    

        if 'comment_sub' in request.POST:
            ProjectComments.objects.create(project_id = proid, comment = request.POST['comment'])

        if 'reportpro_sub' in request.POST:
            ReportedProjects.objects.create(project_id = proid, pro_report = request.POST['reportpro'])

        if 'report_com' in request.POST:
            ReportedComments.objects.create(com_id =int(request.POST['com_id']), com_report = 'Reported Comment')
            

        # canceling project
        # report comments    
        

        return redirect(f'/{args[0]}')
        


