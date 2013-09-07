# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from walk.models import Person, Item
from django.http import HttpResponseRedirect
from django import forms
from django.core.context_processors import csrf
from django.utils import timezone


def info(request, message):
	return render(request, 'walk/info.html', {'message': message})


class ProfileForm(forms.Form):
	name = 	forms.CharField(max_length=50, required=False, label='姓名',)
	CHOICES = (
		('S', '保密'),
		('G', '女生'),
		('B', '男生'),
	)
	sex = forms.CharField(max_length=20, widget=forms.Select(choices=CHOICES), label='性别')
	sign = forms.CharField(max_length=200, required=False, label='签名')
	avatar = forms.ImageField(required=False, label='头像')
	tel = forms.CharField(max_length=20, required=False, label='手机')
	mem = forms.CharField(max_length=200,required=False, label='备忘')

def profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/info/profile-success/')
	else:
		form = ProfileForm()
	c = {'form': form}
	c.update(csrf(request))
	return render(request, 'walk/profile.html', c)

class AddItemForm(forms.Form):
	dest = forms.CharField(max_length=100, label="目的地")
	time = forms.DateTimeField(widget=forms.DateTimeInput(), label="时间")
	subject = forms.CharField(max_length=200, initial="Taxi", label="主题")
	mem = forms.CharField(max_length=200, required=False, label="备忘", widget=forms.Textarea)

def add_item(request):
	if request.method == 'POST':
		form = AddItemForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/info/add-item-success/')
	else:
		form = AddItemForm()
	c = {'form': form}
	c.update(csrf(request))
	return render(request, 'walk/add_item.html', c)

