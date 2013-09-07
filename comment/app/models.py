from django.db import models

class Comment(models.Model):
	pic = models.ImageField(upload_to='photos/%Y/%m/%d')
	text = models.TextField(blank=True, null=True)
	created=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text[:40]

	class Meta:
		ordering = ['-created']