from django.shortcuts import render

# Create your views here.
def NavBar(request):
	return render(request, 'home/base.html')

def home(request):
	return render(request,'home/index.html')

def team1(request):
	return render(request,'home/aboutUs-copy.html')

def team(request):
	return render(request,'home/aboutUs.html')

def team2(request):
	return render(request,'home/aboutUs1.html')

