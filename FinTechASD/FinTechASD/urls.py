from django.conf.urls import url
from django.contrib import admin

#importing views from newsletter app 
from FinTechASD import views as newsletter_views

urlpatterns = [
	#defining url for form
	url(r'^signup/', newsletter_views.signupform),
	
    url(r'^admin/', admin.site.urls),
]