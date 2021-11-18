from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .form import UserForm, ProfileForm


# Create your views here.
def register(request):
    uform = UserForm()
    if request.method == "POST":
        uform = UserForm(request.POST)
        if uform.is_valid:
            u = uform.save(commit=False)
            u.is_active = False
            u.save()
            # send activation code

    context = {
        "uform": uform,
    }
    return render(request, 'add_user.html', context)


def login_fn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            print("dddd")
            login(request, auth)
            # return redirect('/')
    return render(request, 'login.html')


def profile(request):
    pass


def edit_profile(request):
    pass


def logout_fn(request):
    logout(request)
    return redirect('/trainee/login')
