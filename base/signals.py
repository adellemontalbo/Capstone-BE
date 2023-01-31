from django.db.models.signals import pre_save
from django.contrib.auth.models import User

#the object that sends the signal and the instance, and keyword args. This function is just a listener waiting to trigger some action - basically makes our email address our username
def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email


pre_save.connect(updateUser, sender=User)
