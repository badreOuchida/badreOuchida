from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def homapage(request):
	return render(request,'main.html')



def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username,password=password)
		if user is not None :
			login(request,user)
			return redirect('/') 
		else: 
			return HttpResponse('user does not exist') 
	return render(request,'login.html')


def Register(request):
	if request.method == 'POST':

		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2 : 
			user = User(
				username=username,
				email=email,
				password=password1
				)
			user.save()

			login(request,user)
			return redirect('/')
		else :
			return HttpResponse('password does not match')

	return render(request,'register.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/') 