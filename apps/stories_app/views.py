# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import *

from django.contrib import messages

# Create your views here.

def showUser(request):
	if 'email' not in request.session:
		return redirect('/')
	context = {
		'user': User.objects.get(id = request.session['id']),
		'stories': Story.objects.filter(bard = User.objects.get(id = request.session['id']))
	}
	return render(request, 'stories_app/userProfile.html', context)

# def showUser(request):
# 	if 'email' not in request.session:
# 		return redirect('/')
# 	users = User.objects.exclude(id = request.session['id'])
# 	curUser = User.objects.get(id = request.session['id'])
# 	context = {
# 		'users': User.objects.exclude(id = request.session['id'])
# 		'friends': [],
# 		'notFriends': []
# 	}
# 	for user in users:
# 		if user in curUsers.friends.all():
# 			context['friends'].append(user)
# 		else:
# 			context['notFriends'].append(user)
# 	return render(request, 'stories_app/userProfile.html', context)

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









# def register(request):
# 	return render(request, 'loginReg_app/register.html')

# def createUser(request):

# 	results = User.objects.validate(request.POST)

# 	if results['status'] == True:
# 		user = User.objects.creator(request.POST)
# 		messages.success(request, 'Registration successful')

# 	else:
# 		for error in results['errors']:
# 			messages.error(request, error)

# 	return redirect("/")

# def verifyLogin(request):
# 	if 'email' not in request.session:
# 		return redirect('/')
# 	return redirect('/start')


# def login(request):
# 	results = User.objects.loginVal(request.POST)
# 	if results['status'] == False:
# 		messages.error(request, 'Email/password is invalid')
# 		return redirect('/main')
# 	request.session['email'] = results['user'].email
# 	request.session['name'] = results['user'].name
# 	request.session['alias'] = results['user'].alias
# 	request.session['birthday'] = results['user'].birthday
# 	request.session['id'] = results['user'].id
# 	return redirect('/main/directory')

# def directory(request):
# 	if 'email' not in request.session:
# 		return redirect('/main')
# 	return redirect('/friends')