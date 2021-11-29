from django.db import models
from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=400)
    total_target = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    donation = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)
    raters = models.IntegerField(default=0)
    avg_rate = models.FloatField(default=0)

    # category = models.Choices()
    # tags = models.Choices()


class ProjectPics(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='images/')


class ProjectComments(models.Model):
    com_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)    


class ReportedComments(models.Model):
    com_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    com_report = models.CharField(max_length=400)    



class ReportedProjects(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    pro_report = models.CharField(max_length=400)            


class ProjectsTags(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=40)   