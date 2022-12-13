from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=18, default="")
    gender = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    school = models.CharField(max_length=256)
    major = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)

    # TODO 简历

    def __str__(self):
        return self.username
