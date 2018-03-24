from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
	qs = Post.objects.all()

	return render(request,'home.html',{'qs':qs})
	#return HttpResponse('Hello World')