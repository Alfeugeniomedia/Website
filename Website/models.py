from django.db import models
from django.contrib.auth.models import User
from django import forms

class Users(User):

	class Meta:
			verbose_name = 'Users'


class Events(models.Model):
	def __unicode__(self):
	 		return self.title

	title= models.CharField(max_length=30)
	description= models.TextField(max_length=50)
	event_date=models.DateField()
	event_time= models.TimeField()
	# def __unicode__(self):
	# 		return self.content
	# def save(self, **kwargs):
	# 		super(Post, self).save(**kwargs)

class Front_Users(models.Model):
	def __unicode__(self):
	 		return self.name
	SALT_SIZE = 8

	name= models.CharField(max_length=100)
	email= models.CharField(max_length=50)
	password=models.CharField(max_length=255)
	date_joined=models.CharField(max_length=50)
	key=models.TextField(max_length=255)

	
class Membership(models.Model):
	def __unicode__(self):
	 		return self.title
	title=models.CharField(max_length=255)
	price=models.CharField(max_length=100)
	description=models.CharField(max_length=255)


class Member_user(models.Model):
	

	user_id=models.ForeignKey(Front_Users,on_delete=models.CASCADE)
	membership_id=models.ForeignKey(Membership,on_delete=models.CASCADE)
	date=models.DateField()
	expiry_date=models.DateField()

	