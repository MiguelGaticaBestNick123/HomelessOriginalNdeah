from django.contrib import admin
from .models import User, Familiar, Aportador, Residente, Accion, Insumo, CompraInsumo, StockInsumo, Staff

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'f_nacimiento', 'n_telefono', 'email')
    list_editable = ('n_telefono', 'email')

    class Meta:
        model = Familiar

class AportadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'correo', 'telefono', 'nro_tarjeta', 'sexo')
    list_editable = ('direccion', 'correo', 'telefono', 'nro_tarjeta')

    class Meta:
        model = Aportador

class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'f_nacimiento', 'sexo', 'tutor')

    class Meta:
        model = Residente

class CompraInsumoAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra', 'cantidad', 'descripcion', 'insumo', 'proveedor', 'costo_unitario')
    list_editable = ('cantidad', 'descripcion', 'insumo', 'proveedor', 'costo_unitario')

    class Meta:
        model = CompraInsumo

class StaffAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')
    list_editable = ('nombre', 'cargo')
    class Meta:
        model = Staff
    
class AccionAdmin(admin.ModelAdmin):
    list_display = ('residente', 'fecha_hora', 'descripcion')
    list_editable = ('residente', 'fecha_hora', 'descripcion')
    class Meta:
        model = Accion
        
class StockInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'cantidad_stock')
    list_editable = ('insumo', 'cantidad_stock')
    
    class Meta:
        model = StockInsumo
        
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    list_display = ('nombre', 'descripcion')
    class Meta:
        model = Insumo



admin.site.register(User)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Aportador, AportadorAdmin)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(CompraInsumo, CompraInsumoAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Accion, AccionAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(StockInsumo, StockInsumoAdmin)

