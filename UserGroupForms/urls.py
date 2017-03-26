from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userSignup/', views.userSignup),
    url(r'^uploadReport/', views.uploadReport),
    url(r'^groupSignup/', views.groupSignup),

]