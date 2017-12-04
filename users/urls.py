from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
	# log in
	url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]