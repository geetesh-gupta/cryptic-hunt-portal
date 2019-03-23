from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE,
                                limit_choices_to={'is_staff': False})

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profiles'
        verbose_name_plural = 'User Profiles'

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()


post_save.connect(create_profile, sender=User)
