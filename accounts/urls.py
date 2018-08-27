from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("password_reset/",auth_views.password_reset,{'template_name': 'accounts/password_reset_form.html'},name='password_reset'),
    path("password_reset/done/",auth_views.password_reset_done,{'template_name': 'accounts/password_reset_done.html'},name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.password_reset_confirm,{'template_name': 'accounts/password_reset_confirm.html'},name='password_reset_confirm'),
    path("reset/done/",auth_views.password_reset_complete,{'template_name': 'accounts/password_reset_complete.html'},name='password_reset_complete'),
]
