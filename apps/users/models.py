from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # avatar = models.ImageField(upload_to='users/avatar/', null=True, default='default/user/user.png')
 

