from django.contrib import admin
from .models import marca, talla, departamento, prenda, proveedor, venta, cliente

# Register your models here.}
class marcaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class tallaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class departamentoAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class prendaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class proveedorAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class ventaAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

class clienteAdmin(admin.ModelAdmin):
    readonly_fields = ("create", "update")

admin.site.register(marca, marcaAdmin)
admin.site.register(talla, tallaAdmin)
admin.site.register(departamento, departamentoAdmin)
admin.site.register(prenda, prendaAdmin)
admin.site.register(proveedor, proveedorAdmin)
admin.site.register(venta, ventaAdmin)
admin.site.register(cliente, clienteAdmin)
