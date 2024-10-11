from django.contrib import admin
from django.urls import path
from login.views import login_view, home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),



]
