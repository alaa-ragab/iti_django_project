from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=400)
    total_target = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    donation = models.IntegerField(default=0)
    ratings = models.IntegerField(default=0)
    raters = models.IntegerField(default=0)
    avg_rate = models.FloatField(default=0)
    category = models.ForeignKey('ProjectsCategory', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False, null=True)
    tags = models.ManyToManyField('Tags')
    picture = models.ImageField(upload_to='images/')

    @property
    def image_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url


class Tags(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tag)


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


class ProjectsCategory(models.Model):
    category = models.CharField(
        max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.category)


class FeaturedProject(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="featured_project")
    date_featured = models.DateField()

    def __str__(self):
        return self.project.title
