# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from models import User

from django.contrib import messages

# Create your views here.

def home(request):
	if 'email' in request.session:
		return redirect('/user')
	return render(request, 'loginReg_app/home.html')



def register(request):
	return render(request, 'loginReg_app/register.html')



def createUser(request):

	results = User.objects.validate(request.POST)

	if results['status'] == True:
		user = User.objects.creator(request.POST)
		messages.success(request, 'Registration successful')

	else:
		for error in results['errors']:
			messages.error(request, error)

	return redirect("/")



def login(request):
	results = User.objects.loginVal(request.POST)
	if results['status'] == False:
		messages.error(request, 'Email or password is invalid')
		return redirect('/')
	request.session['first_name'] = results['user'].first_name
	request.session['last_name'] = results['user'].last_name
	request.session['alias'] = results['user'].alias
	request.session['birthday'] = results['user'].birthday
	request.session['email'] = results['user'].email
	request.session['id'] = results['user'].id
	return redirect('/user')



def verifyLogin(request):
	if 'email' not in request.session:
		return redirect('/')	
	return redirect('/user')