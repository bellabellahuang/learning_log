"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
	# main page
	url(r'^$', views.index, name='index'),

	# show all topics
	url(r'^topics/$',views.topics, name='topics'),
]