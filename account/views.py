from django.shortcuts import render, redirect
from bigstore import settings

from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User Has been Created')
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')
    else:
        return render(request, 'account/register.html', {"BASE_URL": settings.BASE_URL})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = auth.authenticate(username=username, password=password1)

        if user is not None:
            auth.login(request, user)
            print('login Successfull')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Cedential')
            print('login Failed')
            return redirect('login')

    else:
        return render(request, 'account/login.html', {"BASE_URL": settings.BASE_URL})


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout Successfully')
    return redirect('home')
