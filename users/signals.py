from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User

def createProfile(sender , instance , created , **kwargs):
    user = instance
    profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

def updateUser(sender , instance , created , **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender , instance , created , **kwargs):
    try :
        user = instance.user
        user.delete()
    except :
        pass
    

post_save(createProfile,sender=User)
post_save(updateUser,sender=Profile)
post_delete(deleteUser , sender=Profile)