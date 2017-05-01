from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django_countries.fields import CountryField

# Validate form objects and print error message to template
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    COMPANY = 'COMP'
    INVESTOR = 'INVE'
    USER_TYPE_CHOICES = (
        (COMPANY, 'Company'),
        (INVESTOR, 'Investor'),
       )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
    )
    #siteManager = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

class Report(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1, null = True)
    company_name = models.CharField(max_length = 50, blank = True)
    ceo_name = models.CharField(max_length=50, blank=True)
    company_phone = models.CharField(max_length=11, blank = True)
    company_email = models.CharField(max_length=50, blank=True)
    company_location = models.CharField(max_length=50, blank = True)
    company_country = CountryField()
    sector = models.CharField(max_length=30, blank=True)
    business_type = models.CharField(max_length = 30, blank = True)
    current_projects = models.CharField(max_length = 10, blank = True)
    private = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank = True)
    poodle = models.ManyToManyField('File', blank = True)


class File(models.Model):
    #datetime
    files = models.FileField(upload_to= 'documents/%Y/%m/%d/', blank = True, null = True)
    #file_url = models.CharField(max_length = 100, blank = True)
    report_for_file = models.ForeignKey(Report, related_name="reportFiles", blank = True,  null = True)
