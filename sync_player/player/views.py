from django.shortcuts import render
from django.http import HttpResponse
def admin_page(request):
	f1=open('123456.txt','w');
	f1.close();
	return render(request,'admin.html')
def guest(request):

	return render(request,'guest.html')
# Create your views here.
def get_url(request):
	f=open('video_url.txt','r')
	return HttpResponse(f.read())
def get_time(request):
	f=open('time.txt','r')
	return HttpResponse(f.read())
def set(request):
 	
 	url = request.GET['video_url']
 	CurrentTime = request.GET['CurrentTime'];
 	print(url)
 	f1=open('video_url.txt','w')
 	f1.write(url)
 	f1.close();
 	f1=open('time.txt','w')
 	f1.write(CurrentTime)
 	f1.close()
 	return HttpResponse('success')
 	


