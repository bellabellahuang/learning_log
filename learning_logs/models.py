from django.db import models

# create a class Topic inherit from Model
class Topic(models.Model):
	"""the topic of user learning"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text


