from django.db import models


# Create your models here.


class Company(models.Model):
    email = models.EmailField(unique=True, primary_key=True, default='1@2.3')

    corporation_name = models.CharField(max_length=128)
    corporation_abbreviation = models.CharField(max_length=128)

    corporation_state_of_finance = models.IntegerField(default=-1)
    corporation_size_of_staff = models.IntegerField(default=-1)
    corporation_field = models.CharField(max_length=128)

    corporation_introduction = models.CharField(max_length=1500)

    # corporation_talent_development_list:

    corporation_LRP = models.CharField(max_length=128)
    corporation_setup_time = models.CharField(max_length=128)
    corporation_type = models.IntegerField(default=-1)
    corporation_status = models.IntegerField(default=-1)
    corporation_capital = models.IntegerField(default=0)
    corporation_setup_place = models.CharField(max_length=128)
    corporation_SCC = models.CharField(max_length=128)
    corporation_management_content = models.CharField(max_length=1500)

    corporation_am_time = models.CharField(max_length=128)
    corporation_pm_time = models.CharField(max_length=128)
    corporation_offwork = models.CharField(max_length=128)

    # corporation_welfare_list: ["五险一金", "加班补助", "年终奖"],


class Development(models.Model):
    development_id = models.AutoField(unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)


class Welfare(models.Model):
    welfare_id = models.AutoField(unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)


class Recruiter(models.Model):
    recruiter_id = models.AutoField(unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter_name = models.CharField(max_length=128)
    recruiter_post = models.CharField(max_length=128)


class Job(models.Model):
    job_id = models.AutoField(unique=True, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    position_name = models.CharField(max_length=128)
    position_address = models.CharField(max_length=6)
    position_experience = models.IntegerField(default=-1)
    position_education = models.IntegerField(default=-1)
    position_salary_from = models.IntegerField(default=0)
    position_salary_to = models.IntegerField(default=0)
    position_description = models.CharField(max_length=1500)
