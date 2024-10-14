from django.contrib import admin
from django.urls import path
from login.views import custom_login_view
from home.views import list_orden,ver_examen
from django.contrib.auth import views as auth_views
from user_config.views import user_date
from inf_pdf.views import generar_informe_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', custom_login_view, name='login'),
    path('home/', list_orden, name='home',),
    path('home/<int:id>/', ver_examen, name='ver_examen'),  # Verifica que el nombre sea 'ver_examen'
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('config', user_date, name='config'),
    path('home//<int:orden_id>/', generar_informe_pdf, name='generar_informe_pdf')
    
]
