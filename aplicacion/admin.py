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

admin.site.register(User)
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Aportador, AportadorAdmin)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Accion)
admin.site.register(Insumo)
admin.site.register(CompraInsumo, CompraInsumoAdmin)
admin.site.register(StockInsumo)
admin.site.register(Staff)
