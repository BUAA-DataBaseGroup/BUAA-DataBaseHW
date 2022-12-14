from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class Company(models.Model):
    username = models.CharField(max_length=128, unique=True, primary_key=True)
    company_name = models.CharField(max_length=128, unique=True)
    company_position = models.CharField(max_length=10, default="")
    company_description = models.CharField(max_length=128, default="")
    company_tag1 = models.CharField(max_length=10, default="")
    company_tag2 = models.CharField(max_length=10, default="")
    company_tag3 = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.username + " Company"


class Job(models.Model):
    job_id = models.AutoField(unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=6)
    job_salary_min = models.IntegerField(default=0)
    job_salary_max = models.IntegerField(default=0)
    job_description = models.CharField(max_length=128)
    job_day = models.IntegerField(default=0)
    job_month = models.IntegerField(default=0)
    job_education = models.IntegerField(default=-1, validators=[MaxValueValidator(6), MinValueValidator(-1)])
    contact_name = models.CharField(max_length=128)
    contact_tel = models.CharField(max_length=11)
    contact_info = models.CharField(max_length=10)

    def __str__(self):
        return self.company.username + " Job " + str(self.job_id)
