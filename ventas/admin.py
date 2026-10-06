from django.contrib import admin
from .models import Cliente, Venta

@admin.register(Cliente)
class Clienteadmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "rut", "telefono", "correo")
    list_filter = ("correo",)
    search_fields = ("nombre", "rut")

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display =("id", "fecha", "total_clp", "metodo_pago", "Cliente")
    list_filter =("metodo_pago","fecha")
    search_fields =("metodo_pago", "cliente__nombre")

    @admin.display(description="Total (CLP)", ordering="total")
    def total_clp(self, obj):
        if obj.total is not None:
            return f"${obj.total:,.0f}".replace(",",".")
        return "$0"