from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre
class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    metodo_pago = models.CharField(max_length=50)
    Cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return f"Venta #{self.id} - {self.Cliente.nombre}"
    