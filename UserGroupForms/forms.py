from django import forms
from django.forms import ModelForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from .models import Report
from .models import UserProfile
from django_countries.fields import CountryField
# from uploads.core.models import Report

class UserForm(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_type',)

class ReportForm(forms.ModelForm):
    #report_file_name = forms.CharField(required = False)
    #report_file =  forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}),required = False)
    # company_name = forms.CharField(required = False)
    # company_phone = forms.CharField(required = False)
    # company_location = forms.CharField(required = False)
    # company_country = forms.CharField(required = False)
    # business_type = forms.CharField(required = False)
    #current_projects = forms.CharField(widget= forms.Textarea, label="current_projects",required=True)
    share_with_group = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False)
    # poodle = models.ManyToManyField('File', blank = True)
    #current_projects = forms.ChoiceField(choices=[(x, x) for x in range(0, 100)])
    #memgroups = forms.ModelMultipleChoiceField(queryset=Group.objects.all())
    class Meta:
        model = Report
        fields = ('company_name', 'ceo_name', 'company_phone', 'company_email',
                  'company_location', 'company_country', 'sector', 'business_type',
                  'current_projects','share_with_group', 'private','encrypted', )

    # def save(self):
    #     Report.objects.create(report_file_name="Bill")
    # # # class Meta:
    #     model = Report
    #     fields = ('report_file_name', 'report_file', 'company_name', 'company_phone',
    #               'company_location', 'company_country', 'business_type', 'current_projects', )

class createGroupForm(forms.ModelForm):
    #Select_Users_To_Add_To_Group = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    #depending on company/investor/site manage - see certain users not all()
    class Meta:
        model = Group
        fields = ('name',)
