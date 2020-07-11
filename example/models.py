from django.db import models
from like_system.models import LikesTarget

# Create your models here.


class Test(LikesTarget):
    headline = models.CharField(max_length=500)


class Test1(LikesTarget):
    headline = models.CharField(max_length=500)
