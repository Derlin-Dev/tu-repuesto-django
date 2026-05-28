from rest_framework import serializers
from .models import Proveedor, Repuesto


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProveedorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "id", "nombre", "telefono", "email", "direccion", "estado", "fecha_registro"


class ProveedorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "nombre", "telefono", "email", "direccion", "estado"


class ProveedorUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Proveedor
        fields = "nombre", "telefono", "email", "direccion", "estado"

class ProveedorDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Proveedor
        fields = "id"


class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = '__all__'


class RespuestoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = "codigo_repuesto", "nombre", 
        "descripcion", "categoria", "marca", "modelo_compatible", 
        "unidad_medida", "cantidad_stock", "stock_minimo", "precio_compra", 
        "precio_venta", "ubicacion", "estado", "proveedor_id"
class RepuestoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = "id_repuesto", "codigo_repuesto", "nombre", 
        "descripcion", "categoria", "marca", "modelo_compatible", 
        "unidad_medida", "cantidad_stock", "stock_minimo", "precio_compra", 
        "precio_venta", "ubicacion", "estado", "fecha_registro", "fecha_actualizacion"

class RespuestosUpdateSerializer(serializers.ModelSerializer):
    id_repuesto = serializers.IntegerField()
    class Meta:
        model = Repuesto
        fields = "codigo_repuesto", "nombre", 
        "descripcion", "categoria", "marca", "modelo_compatible", 
        "unidad_medida", "cantidad_stock", "stock_minimo", "precio_compra", 
        "precio_venta", "ubicacion", "estado"

class RepuestoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = "codigo_repuesto", "nombre", 
        "descripcion", "categoria", "marca", "modelo_compatible", 
        "unidad_medida", "cantidad_stock", "stock_minimo", "precio_compra", 
        "precio_venta", "ubicacion", "estado", "proveedor_id"

class RespuestoDeleteSerializer(serializers.ModelSerializer):
    id_repuesto = serializers.IntegerField()
    class Meta:
        model = Repuesto
        fields = "id_repuesto"


