from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your models here.

# Validate form objects and print error message to template
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_type = models.BooleanField(default=False) #user is either admin or not

    def __unicode__(self):
        return self.user.username
    #inheriting from Django Model
    #username, password, email, is active/online
class multipleFiles(models.Model):
    files = models.FileField(upload_to= 'UserGroupForms/', blank = True)

class Report(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    report_file_name = models.CharField(max_length = 20, blank = True)
    report_file = models.ManyToManyField(multipleFiles)
    company_name = models.CharField(max_length = 50, blank = True )
    company_phone = models.CharField(max_length=11, blank = True)
    company_location = models.CharField(max_length=50, blank = True)
    company_country = models.CharField(max_length = 20, blank = True)
    business_type = models.CharField(max_length = 30, blank = True)
    current_projects = models.CharField(max_length= 200, blank = True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank = True)


    def __str__(self):
        return self.report_file_name


# class Group(models.Model):
#     group = models.OneToOneField(Group)
#     def __unicode__(self):
#         return self.group.name

# class Group(models.Model):
#     group_name = models.CharField(max_length=20)
#     group_email = models.CharField(max_length=50)
#     group_password = models.CharField(max_length=30)
#     add_members = models.CharField(max_length=100)
#     remove_members = models.CharField(max_length=100)
