from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^createmessage/', views.sendMessage),
    url(r'^viewmessages/', views.viewMessage),
    url(r'^deletemessages/', views.deleteMessage),

]