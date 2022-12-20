from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True, primary_key=True, default='1@2.3')
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.username
