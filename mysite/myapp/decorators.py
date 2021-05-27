from django.http import HttpResponse
from django.shortcuts import redirect

def unauthen_required(view_func):
	def wrapper_function(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')

		else : 
			return view_func(request,*args,*kwargs)

	return wrapper_function


def OnlySuperUser(view_func):
	def wrapper_function(request,*args,**kwargs):
		if request.user.is_superuser:
			return view_func(request,*args,**kwargs)

		else : 
			return redirect('home')
	return wrapper_function


def AllowByGroup(allowed=[]):
	def wrapper(view_func):
		def func(request,*args,**kwargs):
			group = request.user.groups.all()[0].name

			if group in allowed :
				return view_func(request,*args,**kwargs)
			else : 
				return redirect('home')

		return func(request,*args,**kwargs)
	return wrapper(view_func)	