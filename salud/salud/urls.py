from django.contrib import admin
from django.urls import path
from login.views import custom_login_view
from home.views import list_orden,ver_examen
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', custom_login_view, name='login'),
    path('home/', list_orden, name='home',),
    path('home/<int:id>/', ver_examen, name='ver_examen'),  # Verifica que el nombre sea 'ver_examen'
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
