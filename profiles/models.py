from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True)
    favorite_car_brand = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_c4xbsi'
    )


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
