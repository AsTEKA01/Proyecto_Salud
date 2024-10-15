from django.contrib import admin
from django.urls import path, include
from login.views import custom_login_view
from home.views import list_orden,ver_examen, landing_page_view
from django.contrib.auth import views as auth_views
from user_config.views import user_date
from inf_pdf.views import generar_informe_pdf

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login', custom_login_view, name='login'),
    path('home/', list_orden, name='home',),
    path('home/<int:id>/', ver_examen, name='ver_examen'),  # Verifica que el nombre sea 'ver_examen'
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('config', user_date, name='config'),
    path('home//<int:orden_id>/', generar_informe_pdf, name='generar_informe_pdf'),
    path('', landing_page_view, name="landing"),
    path('captcha/', include('captcha.urls')),  # Incluye las URLs de captcha

    
]
