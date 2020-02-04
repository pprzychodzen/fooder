from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')

    # avatar = models.FileField(upload_to='avatar', blank=True, default='avatar/default-100.png')

    def __str__(self):
        return self.user.username
