from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def image_upload(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'profile_images/user-{instance.user.id}/{filename}'


# Create your models here.

class ProfileModel(models.Model):
    choice = [
        ("Egypt", "Egypt"),
        ("Saudi Arabia", "Saudi Arabia"),
        ("Sudan", "Sudan"),
        ("Tunisia", "Tunisia"),
        ("Algeria", "Algeria"),
        ("Libya", "Libya"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=image_upload, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    Birthdate = models.CharField(max_length=30, blank=True)
    facebook_link = models.URLField(blank=True)
    country = models.CharField(max_length=15, choices=choice, blank=True)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfileModel.objects.create(user=instance, )