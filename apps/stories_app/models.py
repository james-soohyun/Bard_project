# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..loginReg_app.models import User

# Create your models here.

class StoryManager(models.Manager):

	def validate(self, postData):

		results = {
			'status': True,
			'errors': []
		}

		if len(postData['title']) < 1:
			results['errors'].append('Must include title')
			results['status'] = False
		if postData['emotion'] == "Please select emotion":
			results['errors'].append('Must specify emotion')
			results['status'] = False
		if len(postData['content']) < 1:
			results['errors'].append('Story requires content')
			results['status'] = False

		return results




class Story(models.Model):

	title = models.CharField(max_length = 255)
	date = models.DateTimeField(max_length = 10)
	location = models.CharField(max_length = 255)
	emotion = models.CharField(max_length = 255)
	content = models.TextField()
	bard = models.ForeignKey(User, related_name = "stories")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)
	objects = StoryManager()






class CommentManager(models.Manager):

	def validate(self, postData):

		results = {
			'status': True,
			'errors': []
		}

		return results


	def creator(self, postData):
		pass



class Comment(models.Model):

	comment = models.CharField(max_length = 255)
	story = models.ForeignKey(Story, related_name = "comments")
	commentator = models.OneToOneField(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)
	objects = CommentManager()