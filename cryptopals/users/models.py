# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from allauth.socialaccount.models import SocialAccount
import hashlib

from django.core import mail


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    public_key = models.CharField(max_length=100, null=True,\
     blank=True)
    write_about = models.TextField(null=True, blank=True)
    list_user = models.BooleanField(default=True)

    
    def __unicode__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        mail.mail_admins('New cryptopals user', 'New user')

post_save.connect(create_user_profile, sender=User)


# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])