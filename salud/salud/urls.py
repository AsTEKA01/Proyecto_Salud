from django.contrib import admin
from django.urls import path
from login.views import custom_login_view
from home.views import name_sal
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', custom_login_view, name='login'),
    path('home/', name_sal, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
