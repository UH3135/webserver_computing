from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def get_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("why are didn't work?")
        print(user)

        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            request.session['error'] = 'Wrong ID or Password'

    return render(request, 'accounts/login.html', {"status": 'logout'})


@login_required
def get_home_view(request):
    return render(request, 'accounts/home.html', {'user': request.user})


def get_logout_view(request):
    logout(request)
    return redirect('accounts:login')