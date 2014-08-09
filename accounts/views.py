from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from accounts.forms import RegistrationForm, LoginForm
from accounts.models import UserProfile
from django.contrib.auth.models import User


# Create your views here.
@csrf_exempt
def add_user(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['firstName'],
                    last_name=form.cleaned_data['lastName']
                    )
            user.set_password(str(form.cleaned_data['password']))
            user.save()
            user_profile = UserProfile.objects.create(user=user,contact=form.cleaned_data['contact'])
            user_profile.save()
            return HttpResponseRedirect(reverse('login_user'))
        else:
            form=form
            return render(request, 'registration.html',locals())
    else:
        form = RegistrationForm()
        return render(request, 'registration.html',locals())
    pass

@csrf_exempt
def login_user(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                form=form
                return render(request,'registration.html',locals())
        else:
            form=form
            return render(request,'registration.html',locals())
    else:
        form = LoginForm()
        return render(request,'registration.html', locals())

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
