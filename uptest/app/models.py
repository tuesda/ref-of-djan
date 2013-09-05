from django.db import models

# Create your models here.
class Test(models.Model):
	title = models.CharField(max_length=200)
	avatar = models.ImageField(upload_to='photos/%Y/%m/%d')

	def __unicode__(self):
		return self.title