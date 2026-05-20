from django.urls import path
from .views import (
    listar_repuestos,
    crear_repuesto,
    actualizar_repuesto,
    eliminar_repuesto,
    listar_proveedores,
    crear_proveedor,
    actualizar_proveedor,
    eliminar_proveedor
)

urlpatterns = [
    # REPUESTOS
    path('repuestos/', listar_repuestos, name="listar_repuestos"),
    path('repuestos/crear/', crear_repuesto, name="crear_repuesto"),
    path('repuestos/actualizar/<int:id>/', actualizar_repuesto, name="actualizar_repuesto"),
    path('repuestos/eliminar/<int:id>/', eliminar_repuesto, name="eliminar_repuesto"),

    # PROVEEDORES
    path('proveedores/', listar_proveedores, name="listar_proveedores"),
    path('proveedores/crear/', crear_proveedor, name="crear_proveedor"),
    path('proveedores/actualizar/<int:id>/', actualizar_proveedor, name="actualizar_proveedor"),
    path('proveedores/eliminar/<int:id>/', eliminar_proveedor, name="eliminar_proveedor"),
]