from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Transaccion(models.Model):
    TIPOS = [
        ("ingreso", "Ingreso"),
        ("gasto", "Gasto"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return f"{self.usuario} - {self.monto} - {self.tipo}"
