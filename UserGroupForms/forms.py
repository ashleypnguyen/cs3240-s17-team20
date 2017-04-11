from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from .models import Report
from .models import UserProfile

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
    class Meta:
        model = Report
        fields = ('report_file_name', 'report_file', 'company_name', 'company_phone',
                  'company_location', 'company_country', 'business_type', 'current_projects', )

class createGroupForm(forms.ModelForm):
    Select_Users_To_Add_To_Group = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    #depending on company/investor/site manage - see certain users not all()
    class Meta:
        model = Group
        fields = ('name', 'Select_Users_To_Add_To_Group',)
