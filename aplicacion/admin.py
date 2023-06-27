from django.contrib import admin
from .models import Familiar, Aportador, Residente, Accion, Insumo, CompraInsumo, StockInsumo, Plan, Pago, DetallePlan



class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'f_nacimiento', 'n_telefono', 'email')
    list_editable = ('n_telefono', 'email')
    class meta:
        model = Familiar
        

class AportadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'correo', 'telefono', 'sexo')
    list_editable = ('direccion', 'correo', 'telefono', )
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
        
class PlanAdmin (admin.ModelAdmin):
    list_display = ('nombre_plan', 'costo_plan','descripcion_plan')
    class meta:
        model = Plan

class PagoAdmin (admin.ModelAdmin):
    list_display = ('persona', 'tipo_pago','nro_tarjeta','fecha_caducidad', 'titular')
    list_editable = ['titular']
    class meta:
        model = Pago
    
class DetallePlanAdmin (admin.ModelAdmin):
    list_display = ('detallePago', 'detallePlan')
    class meta:
        model = DetallePlan
    
    
admin.site.register(Familiar, FamiliarAdmin)
admin.site.register(Aportador, AportadorAdmin)
admin.site.register(Residente, ResidenteAdmin)
admin.site.register(CompraInsumo, CompraInsumoAdmin)
admin.site.register(Accion, AccionAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(StockInsumo, StockInsumoAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(DetallePlan, DetallePlanAdmin)
