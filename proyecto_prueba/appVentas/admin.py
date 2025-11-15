from django.contrib import admin
from .models import Cliente, Tienda, Compra
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'email')
    search_fields = ('nombre','email')

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('id_tienda', 'nombre', 'direccion')
    search_fields = ('nombre','direccion')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin): 
    list_display = ('id_compra', 'cliente', 'tienda', 'fecha', 'monto')
    search_fields = ('cliente__nombre', 'tienda__nombre')
    list_filter = ('fecha', 'tienda')
    autocomplete_fields = ('cliente', 'tienda')
    
