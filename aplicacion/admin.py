from django.contrib import admin
from .models import Familiar, Aportador, Residente, Accion, Insumo, CompraInsumo, StockInsumo



class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'f_nacimiento', 'n_telefono', 'email')
    list_editable = ('n_telefono', 'email')
    class meta:
        model = Familiar
        

class AportadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'correo', 'telefono', 'nro_tarjeta', 'sexo')
    list_editable = ('direccion', 'correo', 'telefono', 'nro_tarjeta')
    class meta:
        model = Aportador

class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'f_nacimiento', 'sexo', 'tutor')
    class meta:
        model = Residente

class CompraInsumoAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra', 'cantidad', 'descripcion', 'insumo', 'proveedor', 'costo_unitario')
    list_editable = ('cantidad', 'descripcion', 'insumo', 'proveedor', 'costo_unitario')
    class meta:
        model = CompraInsumo

class AccionAdmin(admin.ModelAdmin):
    list_display = ('residente', 'fecha_hora', 'descripcion')
    list_editable = ('fecha_hora', 'descripcion')
    list_display_links = ('residente',)  # Agrega esta línea
    class meta:
        model = Accion
        
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    class meta:
        model = Insumo


class StockInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'cantidad_stock')
    list_editable = ('cantidad_stock',)
    list_display_links = ('insumo',)  # Agrega esta línea
    class meta:
        model = StockInsumo


admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Aportador, AportadorAdmin)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(CompraInsumo, CompraInsumoAdmin)
admin.site.register(Accion, AccionAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(StockInsumo, StockInsumoAdmin)
