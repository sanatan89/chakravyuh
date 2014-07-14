from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    contact = models.IntegerField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    signup_source = models.CharField(max_length=20, blank=True)
    score = models.IntegerField(null=True, default=0)
    