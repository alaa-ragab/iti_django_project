from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from .form import UserForm, ProfileForm
from .models import ProfileModel
from django.http import HttpResponse


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
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth = authenticate(request, email=email, password=password)
        if auth is not None:
            login(request, auth)
            # return redirect('/')
    return render(request, 'login.html')


def profile(request):
    profile_obj = ProfileModel.objects.get(user=request.user)
    print(profile_obj)
    context = {
        "profile": profile_obj
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile_obj = ProfileModel.objects.get(user=request.user)
    profileform = ProfileForm(instance=profile_obj)
    if request.method == "POST":
        profileform = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if profileform.is_valid:
            profileform.save()
            return redirect("accounts:profile")
    context = {
        "profileform": profileform,
        "profile_obj": profile_obj
    }

    return render(request, 'edit_profile.html', context)


def logout_fn(request):
    logout(request)
    return redirect('accounts:login')


# pattern against ^01[0-2]\d{8}$

"""def change_password(request):
    pform = PasswordChangeForm(request.user)
    if request.method == "POST":
        pform = PasswordChangeForm(request.POST, request.user)
        if pform.is_valid:
            pform.save()
            return redirect("accounts:profile")
    context = {
        "change_pass_form": pform
    }
    return render(request, 'password_change_form.html', context)
"""
