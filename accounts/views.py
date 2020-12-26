from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You Successfully logOut')
        return redirect('index')


def register(request):
    if request.method == 'POST':
        # Get All The value
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Checking the username
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # for direct redirect to home page
                    # user.save()
                    # auth.login(request, user)
                    # messages.success(request, 'You are logged in.')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registerd and can login')
                    return redirect('login')

        else:
            messages.error(request, 'Password Not Match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
