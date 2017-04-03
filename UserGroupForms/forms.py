from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Report
from .models import Group
from .models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_file_name', 'report_file', 'company_name', 'company_phone',
                  'company_location', 'company_country', 'business_type', 'current_projects', )

class createGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_name', 'add_members', 'remove_members')

#class editGroupForm(forms.ModelForm):
    #class Meta:
    #    model = edit_group
    #    fields = ('group_name', 'add_members', 'remove_members', 'delete_group')