from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class Resume(models.Model):
    username = models.CharField(max_length=128, unique=True, primary_key=True)
    my_name = models.CharField(max_length=128)
    my_status = models.IntegerField(default=-1, validators=[MaxValueValidator(3), MinValueValidator(-1)])
    my_sex_is_male = models.BooleanField(default=True)
    my_birth = models.CharField(max_length=10, default="")
    my_tel = models.CharField(max_length=11, default="")
    my_date_of_first_work = models.CharField(max_length=7, default="")
    my_wechat = models.CharField(max_length=128, default="")
    my_email = models.EmailField(unique=True)

    my_advantage = models.TextField(max_length=200, default="")

    my_expect_work_type = models.IntegerField(default=0, validators=[MaxValueValidator(2), MinValueValidator(0)])
    my_expect_work_place = models.CharField(max_length=6, default="")
    my_expect_work_position = models.CharField(max_length=6, default="")
    my_expect_work_field = models.CharField(max_length=10, default="")
    my_expect_salary = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.username + " Resume"


class Work(models.Model):
    work_id = models.AutoField(unique=True, primary_key=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    company_field = models.CharField(max_length=10)
    company_department = models.CharField(max_length=10)
    company_position = models.CharField(max_length=6)
    company_start = models.CharField(max_length=7)
    company_end = models.CharField(max_length=7)
    company_content = models.CharField(max_length=1500)
    company_achievement = models.CharField(max_length=300)

    def __str__(self):
        return self.resume.username + " Work " + str(self.work_id)


class Item(models.Model):
    item_id = models.AutoField(unique=True, primary_key=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    username = models.CharField(max_length=256)
    item_name = models.CharField(max_length=20)
    item_role = models.CharField(max_length=10)
    item_link = models.CharField(max_length=6)
    item_start = models.CharField(max_length=7)
    item_end = models.CharField(max_length=7)
    item_description = models.CharField(max_length=1500)
    item_achievement = models.CharField(max_length=200)

    def __str__(self):
        return self.resume.username + " Item " + str(self.item_id)


class Education(models.Model):
    education_id = models.AutoField(unique=True, primary_key=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    education_name = models.CharField(max_length=20)
    education_record = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0)])
    education_subject = models.CharField(max_length=20)
    education_start = models.CharField(max_length=7)
    education_end = models.CharField(max_length=7)
    education_experience = models.CharField(max_length=1500)

    def __str__(self):
        return self.resume.username + " Work " + self.education_name
