from django.contrib import admin
from app.models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ['pic','text', ]

admin.site.register(Comment,CommentAdmin)