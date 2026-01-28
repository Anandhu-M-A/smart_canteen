from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

