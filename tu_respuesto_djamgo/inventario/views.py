from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Repuesto, Proveedor
from .serializers import RepuestoSerializer, ProveedorSerializer

from django.db.models import Q


# ==============================
# REPUETO (INVENTARIO)
# ==============================

# LISTAR REPUESTOS (con filtro categoría y búsqueda por código)
@api_view(['GET'])
def listar_repuestos(request):
    repuestos = Repuesto.objects.all()

    codigo = request.query_params.get("codigo")
    categoria = request.query_params.get("categoria")

    if codigo:
        repuestos = repuestos.filter(codigo_repuesto__icontains=codigo)

    if categoria:
        repuestos = repuestos.filter(categoria__icontains=categoria)

    serializer = RepuestoSerializer(repuestos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# CREAR REPUESTO
@api_view(['POST'])
def crear_repuesto(request):
    serializer = RepuestoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ACTUALIZAR REPUESTO
@api_view(['PUT'])
def actualizar_repuesto(request, id):
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id)
    except Repuesto.DoesNotExist:
        return Response({"error": "Repuesto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RepuestoSerializer(repuesto, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ELIMINAR REPUESTO
@api_view(['DELETE'])
def eliminar_repuesto(request, id):
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id)
    except Repuesto.DoesNotExist:
        return Response({"error": "Repuesto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    repuesto.delete()
    return Response({"mensaje": "Repuesto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)


# ==============================
# PROVEEDOR
# ==============================

# LISTAR PROVEEDORES (con búsqueda)
@api_view(['GET'])
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()

    buscar = request.query_params.get("buscar")

    if buscar:
        proveedores = proveedores.filter(
            Q(nombre__icontains=buscar) |
            Q(email__icontains=buscar) |
            Q(telefono__icontains=buscar)
        )

    serializer = ProveedorSerializer(proveedores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# CREAR PROVEEDOR
@api_view(['POST'])
def crear_proveedor(request):
    serializer = ProveedorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ACTUALIZAR PROVEEDOR
@api_view(['PUT'])
def actualizar_proveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({"error": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProveedorSerializer(proveedor, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ELIMINAR PROVEEDOR
@api_view(['DELETE'])
def eliminar_proveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({"error": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    proveedor.delete()
    return Response({"mensaje": "Proveedor eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)