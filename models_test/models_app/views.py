#-*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django import forms
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
	return render(request, 'models_app/index.html')

def success(request, message):
	return render(request, 'models_app/success.html', {'message': message,})

class LogInForm(forms.Form):
	username = forms.CharField(max_length=50, label='用户名')
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, label='密码')

def auth_login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = LogInForm(request.POST)
			if form.is_valid():
				username = request.POST['username']
				password = request.POST['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect('/success/loginsuccess/')
					else:
						return HttpResponseRedirect('/success/userisnotactive/')
				else:
					return HttpResponseRedirect('/success/notcorrect/')
		else:
			form = LogInForm()
		a = {'form': form}
		a.update(csrf(request))
		return render(request, 'models_app/login.html',a)
	else:
		return HttpResponseRedirect('/success/alreadylogin/')

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

class LogUpForm(forms.Form):
	username = forms.CharField(max_length=50, error_messages={'required':'缺少用户名'},label='用户名')
	email = forms.EmailField(error_messages={'required':'请输入电子邮件','invalid':'格式不正确'}, label='邮件')
	password = forms.CharField(max_length=32, widget=forms.PasswordInput,label='设置密码')
	password_again = forms.CharField(max_length=32, widget=forms.PasswordInput, label='确认密码')


def logup(request):
	if request.method == 'POST':

		form = LogUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			password_again = form.cleaned_data['password_again']
			if password == password_again:
				user = User.objects.create_user(username, email, password)
				user.save()
				test = authenticate(username=username, password=password)
				login(request, test)
				return HttpResponseRedirect('/success/logup/')
			else:
				password.error_messages[required]='hahah'
	else:
		form = LogUpForm()

	a = {'form': form}
	a.update(csrf(request))


	return render(request, "models_app/logup.html", a)