from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    is_online = models.BooleanField(default=False)
