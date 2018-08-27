"""final_social_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("test/", views.TestPage.as_view(), name="test"),
    path("thanks/", views.ThanksPage.as_view(), name="thanks"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("groups/",include("groups.urls", namespace="groups")),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]