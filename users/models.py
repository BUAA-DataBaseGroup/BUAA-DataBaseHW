from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=128, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.username
