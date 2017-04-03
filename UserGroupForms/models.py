from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Validate form objects and print error message to template
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username

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


