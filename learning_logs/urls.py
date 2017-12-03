"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
	# main page
	url(r'^$', views.index, name='index'),

	# show all topics
	url(r'^topics/$',views.topics, name='topics'),

	# show all information within a specific topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# new entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')
]