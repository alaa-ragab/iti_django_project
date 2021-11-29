from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .form import UserForm, ProfileForm
from .models import ProfileModel
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import generate_token


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
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth = authenticate(email=email, password=password)
        print(auth)
        if auth is not None:
            login(request, auth)
            print("ssss")
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
            return redirect("profile")
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
