from django.contrib import admin
from django.urls import path
from login.views import custom_login_view, home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', custom_login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]