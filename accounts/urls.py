from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_fn, name="login"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('logout/', views.logout, name="logout")
]
