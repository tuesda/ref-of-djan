from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect,HttpResponse
from app.models import Comment
from django import forms

def info(request, message):
	return render(request,'app/info.html',{'message': message})

class CommentForm(forms.Form):
	text = forms.CharField(required=False, max_length=200, widget=forms.Textarea)
	pic = forms.ImageField()

def comment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			text = form.cleaned_data['text']
			pic = request.FILES['pic']
			comment = Comment(text=text, pic=pic)
			comment.save()
			import Image
			im = Image.open(comment.pic)
			im = im.resize((im.size[0]/4, im.size[1]/4), Image.ANTIALIAS)
			from django.conf import settings
			path = settings.MEDIA_ROOT+comment.pic.name
			im.save(path)
			return HttpResponseRedirect('/info/ok/')
	else:
		form = CommentForm()
	c = {'form': form}
	c.update(csrf(request))

	return render(request,'app/comment.html',c)

def comment_list(request):
	comments = Comment.objects.all()
	return render(request, 'app/comment_list.html', {'comments':comments})