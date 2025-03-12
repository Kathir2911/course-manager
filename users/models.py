from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
