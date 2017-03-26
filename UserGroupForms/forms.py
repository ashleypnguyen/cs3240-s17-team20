from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User
from .models import Report
from .models import Group


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_name', 'password', 'user_type')

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