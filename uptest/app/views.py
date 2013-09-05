# Create your views here.
from app.models import Test
from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=200)
	avatar = forms.ImageField()

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			'''handle_upload_file(request.FILES['file'])'''
			title = form.cleaned_data['title']
			avatar = request.FILES['avatar']
			test = Test(title=title, avatar=avatar)
			test.save()
			import Image
			im = Image.open(test.avatar)
			im = im.resize((im.size[0]/4,im.size[1]/4), Image.ANTIALIAS)
			from django.conf import settings
			path = settings.MEDIA_ROOT+test.avatar.name
			im.save(path)
			return render(request, 'ok.html')
	else:
		form = UploadFileForm()
	c = {'form': form}
	c.update(csrf(request))
	return render(request, 'upload.html', c)
	