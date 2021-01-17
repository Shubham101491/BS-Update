from django.shortcuts import render, redirect
from bigstore import settings

from account.forms import RegisterForm, UserForm

from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.info(request, 'User Has been Created')
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')
    else:
        register_form = RegisterForm()
        return render(request, 'account/register.html', {"BASE_URL": settings.BASE_URL, 'register_form': register_form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credential")
            return redirect('login')
    else:
        user_form = UserForm()
        return render(request, 'account/login.html', {"BASE_URL": settings.BASE_URL, 'user_form': user_form})


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout Successfully')
    return redirect('home')
