from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#
class MessageForm(forms.Form):
    from_name = forms.CharField()
    to_name = forms.CharField()
    message_content = forms.CharField()

#     # class Meta:
#     #     model = Message
#     #     fields = ('from_name', 'to_name', 'message_content')
