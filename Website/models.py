from django.db import models
from django.contrib.auth.models import User


class Users(User):

    class Meta:
        verbose_name = 'Users'



