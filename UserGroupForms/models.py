from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user_type = models.CharField(max_length=30)

class Report(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    report_file_name = models.CharField(max_length = 20)
    report_file = models.FileField(upload_to='documents/')
    company_name = models.CharField(max_length = 50)
    company_phone = models.CharField(max_length=11)
    company_location = models.CharField(max_length=50)
    company_country = models.CharField(max_length = 20)
    business_type = models.CharField(max_length = 30)
    current_projects = models.CharField(max_length= 200)

class Group(models.Model):
    group_name = models.CharField(max_length=20)
    add_members = models.CharField(max_length=100)
    remove_members = models.CharField(max_length=100)

