from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.lista_clientes, name='lista_clientes'),
    path("nuevo_cliente/", views.crear_cliente, name="crear_cliente"),
    path("eliminar_cliente/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),
    path("actualizar_cliente/<int:id>/", views.actualizar_cliente, name='actualizar_cliente'),
    path('', views.pagina_inicio, name='inicio'),
    path('ru-obs/', views.vista_ru_obs, name='ru_obs'),
    path('login/', views.login_personalizado, name='login'),
    path('logout/', views.logout_personalizado, name='logout'),
]