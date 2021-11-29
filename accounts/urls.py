from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetDoneView
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_fn, name="login"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),

    path('password_change/',
         PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),
         name='password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
         name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),

    path('reset/done/',
         PasswordChangeDoneView.as_view(template_name="registration/password_reset_complete.html"),
         name='password_reset_complete'),

    path('logout/', views.logout_fn, name="logout"),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
]

'''
'''
