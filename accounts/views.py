from django.shortcuts import render_to_response, redirect, RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login


def login_user(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    errors = []
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
            else:
                errors.append({'message': "Your account has been disabled"})
        else:
            errors.append({'message': "The username and password you have entered do not match our records"})
    return render_to_response("login.html", {'errors': errors}, RequestContext(request))


def register(request):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    errors = []
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        email = request.POST['email']
        if not username:
            errors.append({'message': "You need to enter a username"})
        if not email:
            errors.append({'message': "you need to enter an email address"})
        if password and password != confirm:
            errors.append({'message': 'Your passwords do not match!'})
        if not errors:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect(reverse('login'))
            except Exception as ex:
                errors.append({'message': ex})

    return render_to_response("register.html", {'errors': errors}, RequestContext(request))
