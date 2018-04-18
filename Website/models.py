from django.db import models
from django.contrib.auth.models import User
from django import forms

class Users(User):

	class Meta:
			verbose_name = 'Users'


class EventsForm(models.Model):

	title= models.CharField(max_length=30)
	description= models.TextField(max_length=50)
	event_date=models.CharField(max_length=50)

	# def __unicode__(self):
	# 		return self.content
	# def save(self, **kwargs):
	# 		super(Post, self).save(**kwargs)



