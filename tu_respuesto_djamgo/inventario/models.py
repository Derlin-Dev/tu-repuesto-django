from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=15, default="Activo")
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Repuesto(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    id_repuesto = models.AutoField(primary_key=True)
    codigo_repuesto = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)

    categoria = models.CharField(max_length=50, null=True, blank=True)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo_compatible = models.CharField(max_length=100, null=True, blank=True)

    unidad_medida = models.CharField(max_length=20, default="Unidad")

    cantidad_stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=0)

    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    ubicacion = models.CharField(max_length=50, null=True, blank=True)

    proveedor_id = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name="repuestos"
    )

    estado = models.CharField(max_length=15, choices=ESTADOS, default="Activo")

    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo_repuesto} - {self.nombre}"