# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import *

from ..loginReg_app.models import User

from django.contrib import messages

# Create your views here.

def showProfile(request):
	if 'email' not in request.session:
		return redirect('/')
	context = {
		'user': User.objects.get(id = request.session['id']),
		'stories': Story.objects.filter(bard = User.objects.get(id = request.session['id']))
	}
	return render(request, 'stories_app/userProfile.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')

def newStory(request):
	return render(request, 'stories_app/newPost.html')

def dashboard(request):

	if 'email' not in request.session:

			return redirect('/')

	context = {

		'user': User.objects.get(id = request.session['id']),
		'stories': Story.objects.all()
	}

	return render(request, 'stories_app/dashboard.html', context)

def postStory(request):
	
	results = Story.objects.validate(request.POST)

	if results['status'] == True and request.method == 'POST':

		story = Story.objects.create(title = request.POST['title'], date = request.POST['date'], location = request.POST['location'], emotion = request.POST['emotion'], content = request.POST['content'], bard = User.objects.get(id = request.session['id']))

	else:

		for error in results['errors']:

			messages.error(request, error)

	return redirect('/user/')

def bardProfile(request, user_id):

	context = {

		'curUser': User.objects.get(id = request.session['id']),
		'user': User.objects.get(id = user_id),
		'stories': Story.objects.filter(bard = User.objects.get(id = user_id))

	}

	return render(request, 'stories_app/bardProfile.html', context)

def follow(request, user_id):

	if 'email' not in request.session:
		return redirect('/')

	curUser = User.objects.get(id = request.session['id'])
	friendUser = User.objects.get(id = user_id)
	curUser.followers.add(friendUser)
	messages.success(request, "You are following {}".format(friendUser.alias))
	return redirect('')

def unfollow(request, user_id):

	if 'email' not in request.session:
		return redirect('/')

	curUser = User.objects.get(id = request.session['id'])
	friendUser = User.objects.get(id = user_id)
	curUser.followers.remove(friendUser)
	messages.success(request, "You are no longer following {}".format(friendUser.alias))
	return redirect('')

# def dashboard(request):
# 	if 'email' not in request.session:
# 		return redirect('/main')
# 	users = User.objects.exclude(id = request.session['id'])
# 	curUser = User.objects.get(id = request.session['id'])
# 	context = {
# 		'users': User.objects.exclude(id = request.session['id']),
# 		'friends': [],
# 		'notFriends': []
# 	}
# 	for user in users:
# 		if user in curUser.friends.all():
# 			context['friends'].append(user)
# 		else:
# 			context['notFriends'].append(user)
# 	return render(request, 'users_app/users.html', context)

# def logout(request) :
# 	request.session.flush()
# 	return redirect('/main')

# def display(request, user_id):
# 	if 'email' not in request.session:
# 		return redirect('/main')
# 	context = {
# 		'user': User.objects.get(id = user_id),
# 	}
# 	return render(request, 'users_app/profile.html', context)

# def addFriend(request, user_id):
# 	if 'email' not in request.session:
# 		return redirect('/main')
# 	curUser = User.objects.get(id = request.session['id'])
# 	friendUser = User.objects.get(id = user_id)
# 	curUser.friends.add(friendUser)
# 	messages.success(request, 'You are now friends with {}'.format(friendUser.alias))
# 	return redirect('/friends')

# def removeFriend(request, user_id):
# 	if 'email' not in request.session:
# 		return redirect('/main')
# 	curUser = User.objects.get(id = request.session['id'])
# 	friendUser = User.objects.get(id = user_id)
# 	curUser.friends.remove(friendUser)
# 	messages.success(request, 'You are no longer friends with {}'.format(friendUser.alias))
# 	return redirect('/friends')
