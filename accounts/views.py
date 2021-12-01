from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .form import UserForm, ProfileForm
from .models import ProfileModel
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .utils import generate_token
from django.contrib.auth.decorators import login_required


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email])
    print(email)


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# Create your views here.
def register(request):
    uform = UserForm()
    if request.method == "POST":
        uform = UserForm(request.POST)
        print(uform.errors)
        if uform.is_valid:
            u = uform.save(commit=False)
            u.is_active = False
            u.save()
            print(u.email)
            send_activation_email(u, request)

    context = {
        "uform": uform,
    }
    return render(request, 'add_user.html', context)


def login_fn(request):
    if request.user.is_authenticated:
        return redirect('project:viewall')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            auth = authenticate(username=email, password=password)

            if auth is not None:
                login(request, auth)
                print("ssss")
                return redirect('project:viewall')
    return render(request, 'login.html')


@login_required(login_url='login')
def profile(request):
    profile_obj = ProfileModel.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)

    context = {
        "profile": profile_obj,
        "user": user
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    user = User.objects.get(username=request.user.username)
    profile_obj = ProfileModel.objects.get(user=request.user)
    profileform = ProfileForm(instance=profile_obj)

    if request.method == "POST":
        profileform = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        if profileform.is_valid():
            profileform.save()
            print(fname, lname, username)
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.save()
            return redirect("profile")

    context = {
        "form": profileform,
        "user": user,
        "profile": profile_obj
    }

    return render(request, 'edit_profile.html', context)


@login_required(login_url='login')
def delete_user(request):
    password = request.POST.get('password')
    auth = authenticate(username=request.user.email, password=password)
    print(request.user.email)
    print(password)
    print(auth)
    if auth is not None:
        User.objects.get(username=request.user.username).delete()
        return HttpResponse("account delete successfully")
    else:
        return redirect("profile")


@login_required(login_url='login')
def logout_fn(request):
    logout(request)
    return redirect('login')


def test(request):
    return redirect('login')

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
