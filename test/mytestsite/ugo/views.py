from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,'123.html',locals())
def login(request):

    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html') 
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')