from django.shortcuts import render
from django.contrib.auth.models import User , Group 
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .decorators import unauthen_required ,OnlySuperUser

from .models import Apply

# Create your views here.
@login_required

def homapage(request):
	user = request.user
	group = user.groups.all()
	is_True = ('geran' == group[0].name )
	is_speruser = user.is_superuser
	return render(request,'main.html',{'name':group,'is_true':is_True , 'is_speruser':is_speruser})



@unauthen_required
def Login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		user = authenticate(request, username=username, password=password)
		if user is not None :
			login(request,user)
			return redirect('home')

	return render(request,"login.html")



@unauthen_required
def Register(request):


	if request.method == 'POST':

		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		print(username,password1)
		try :
			users = User.objects.get(username=username)
		except ObjectDoesNotExist:
			users = None
		try :
			users = User.objects.get(email=email)
		except ObjectDoesNotExist:
			users = None

		if (users == None ) and (password1 == password2) : 

			user =User.objects.create(
				username = username,
				email =email,
				)

			user.set_password(password1)
			
			user.save()

			group,group_created = Group.objects.get_or_create(name='customer')



			user.groups.add(group)


			user.save()



			login(request,user)
			return redirect('home')

		elif (users!=None):	
			return HttpResponse('username or email already exist')

		elif (password1 != password2):
			return HttpResponse('password does not match')


	return render(request,"register.html")

@login_required
def logout_view(request):
	logout(request)
	return redirect('register')

@login_required
def Switch(request):

	user = request.user
	group = user.groups.all()
	
	current = group[0].name
	if 'geran' == current:
		user.groups.clear()
		group,group_created = Group.objects.get_or_create(name='customer')
		user.groups.add(group)
		print('geran')

	elif 'customer' == current:
		user.groups.clear()
		group,group_created = Group.objects.get_or_create(name='geran')
		user.groups.add(group)
		print('customer')
		

	user.save()

	return redirect('home')


@login_required
def ApplyView(request):

	Apply.objects.create(
		user=request.user,
		)
	
	return redirect('home')


@login_required
@OnlySuperUser
def details(request):
	try :
		users = Apply.objects.filter(appled=True)
	except ObjectDoesNotExist :
		return HttpResponse('no appled users')

	return render(request,'details.html',{'users':users})




@login_required
@OnlySuperUser
def Accepte(request,pk):
	try :
		user = Apply.objects.get(pk=pk)
	except ObjectDoesNotExist :
		return HttpResponse('no appled users')

	user.user.is_superuser = True
	user.user.save()
	user.delete()
	return redirect('de')




@login_required
@OnlySuperUser
def Remove(request,pk):
	try :
		user = Apply.objects.get(pk=pk)
		print(user)
	except ObjectDoesNotExist :
		return HttpResponse('no appled users')
	
	user.delete()
	return redirect('de')


