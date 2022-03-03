from cProfile import Profile
from django.contrib import messages
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_delete,post_save


@receiver(post_save,sender=User)
def createProfile(sender,created, instance,**kwargs):
    if created:
        user = instance
        profile = UserProfile.objects.create(
            user = user,
            first_name = user.first_name,
            last_name = user.last_name,
            username = user.username,
            email = user.email,
        )

@receiver(post_delete, sender=UserProfile)
def deleteProfile(sender,instance,**kwargs):
    instance.delete()