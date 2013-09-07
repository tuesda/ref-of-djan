from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Person(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	sex = models.CharField(max_length=20)
	sign = models.CharField(max_length=200, blank=True, null=True)
	avatar = models.FileField(upload_to='photos/%Y/%m/%d')
	tel = models.CharField(max_length=20, blank=True, null=True)
	mem = models.CharField(max_length=200,blank=True, null=True)

	def __unicode__(self):
		return self.user


class Item(models.Model):
	dest = models.CharField(max_length=100)
	time = models.DateTimeField()
	pub_time = models.DateTimeField(default=timezone.now())
	subject = models.CharField(max_length=200,default='Taxi together')
	person_one = models.ForeignKey(Person, related_name='one_set')
	person_two = models.ForeignKey(Person, related_name='two_set', blank=True, null=True)
	person_three = models.ForeignKey(Person, related_name='three_set', blank=True, null=True)
	person_four = models.ForeignKey(Person, related_name='four_set', blank=True, null=True)
	mem_one = models.CharField(max_length=200, blank=True, null=True)
	mem_two = models.CharField(max_length=200, blank=True, null=True)
	mem_three = models.CharField(max_length=200, blank=True, null=True)
	mem_four = models.CharField(max_length=200, blank=True, null=True)
	is_active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Go "+self.dest+" at "+self.time

	class Meta:
		ordering = ['-pub_time']





