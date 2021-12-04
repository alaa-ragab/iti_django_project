from django.db import models
from django.contrib.auth.models import User

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "images/%s.%s"%(instance.title,extension)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=400)
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
    image = models.ImageField(upload_to=image_upload,blank=True, null=True)
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
          return self.image.url



class ProjectsTags(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    tags = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tags)


class ProjectPics(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to=image_upload)


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
    categories = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.categories)


class FeaturedProject(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="featured_project")
    date_featured = models.DateField()

    def __str__(self):
        return self.project.title
