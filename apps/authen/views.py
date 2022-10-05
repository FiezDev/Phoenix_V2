from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_view(request):
    # logout(request)
    # username = ''
    # password = ''
    # if request.POST:
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     context = {
    #         'username': username,
    #         'password' : password
    #     }

    #     user = authenticate(username=username, password=password)
    #     if user is not None or user.is_active:
    #         login(request, user)
    #         return HttpResponseRedirect('phoenix/dashboard')
    return render(request,"registrations/login.html", context)

def twofa_view(request):
    return render(request,"registrations/2fa.html",{})
