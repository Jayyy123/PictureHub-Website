from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    default_id = models.UUIDField(default=uuid.uuid1)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False, blank=False, default='firstname {}'.format(default_id))
    last_name = models.CharField(max_length=100, null=False, blank=False, default='lastname')
    username = models.CharField(max_length=100, null=False, blank=False, default='user')
    profile_picture = models.ImageField(default='user.jpeg')
    bio = models.TextField(default=True, blank=True)
    description = models.TextField(default=True, blank=True)
    email = models.EmailField(default='useremail', blank=False, null=False)
    social_links = models.OneToOneField('Socials', on_delete=models.CASCADE, null=True, blank=True)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self) -> str:
        return self.username


class Socials(models.Model):
    linkedin = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)
    slack = models.URLField(blank=True,null=True)
    stack_overflow = models.URLField(blank=True,null=True)
    add = models.OneToOneField('AddSocials', on_delete=models.CASCADE, blank=True, null=True)


class AddSocials(models.Model):
    name = models.CharField(max_length=80, blank=True, null= True)
    link = models.URLField(blank=True, null=True)



