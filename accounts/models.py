from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):
    superadmin = ('superadmin', 'SuperAdmin')
    admin = ('admin', 'Admin')
    user = ('user', 'User')

class User(AbstractUser):
    
    role = models.CharField(max_length=10, choices=UserRoles.choices, default='user')

    def is_superadmin(self):
        return self.role == 'superadmin'

    def is_admin(self):
        return self.role in ('superadmin', 'admin')

    def is_regular_user(self):
        return self.role == 'user'