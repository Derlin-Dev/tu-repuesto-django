from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Repuesto, Proveedor
from .serializers import  RepuestoSerializer, ProveedorSerializer, ProveedorUpdateSerializer, RepuestoCreateSerializer , RespuestosUpdateSerializer, ProveedorDeleteSerializer, RepuestoDetailSerializer, ProveedorDetailSerializer, ProveedorCreateSerializer, ProveedorDeleteSerializer , RepuestoCreateSerializer, RepuestoDetailSerializer

from django.db.models import Q

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


@api_view(['POST'])
def crear_repuesto(request):
    codigo_repuesto = request.data.get("codigo_repuesto")
    nombre = request.data.get("nombre")
    proveedor_id = request.data.get("proveedor_id")
    descripcion = request.data.get("descripcion")
    categoria = request.data.get("categoria")
    marca = request.data.get("marca")
    modelo_compatible = request.data.get("modelo_compatible")
    unidad_medida = request.data.get("unidad_medida")
    cantidad_stock = request.data.get("cantidad_stock")
    stock_minimo = request.data.get("stock_minimo")
    precio_compra = request.data.get("precio_compra")
    precio_venta = request.data.get("precio_venta")
    ubicacion = request.data.get("ubicacion")
    estado = request.data.get("estado")

    if Repuesto.objects.filter(codigo_repuesto=codigo_repuesto).exists():
        return Response({"error": "El código de repuesto ya existe"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not Proveedor.objects.filter(id=proveedor_id).exists():
        return Response({"error": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    repuesto = Repuesto.objects.create (
        codigo_repuesto=codigo_repuesto,
        nombre=nombre,
        proveedor_id=proveedor_id,
        descripcion=descripcion,
        categoria=categoria,
        marca=marca,
        modelo_compatible=modelo_compatible,
        unidad_medida=unidad_medida,
        cantidad_stock=cantidad_stock,
        stock_minimo=stock_minimo,
        precio_compra=precio_compra,
        precio_venta=precio_venta,
        ubicacion=ubicacion,
        estado=estado
    )
    serializer = RepuestoCreateSerializer(repuesto)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def actualizar_repuesto(request, id):

    try:
        repuesto = Repuesto.objects.get(id_repuesto=id)
    except Repuesto.DoesNotExist:
        return Response({"error": "Repuesto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = RespuestosUpdateSerializer(repuesto, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_repuesto(id):
    try:
        repuesto = Repuesto.objects.get(id_repuesto=id)
    except Repuesto.DoesNotExist:
        return Response({"error": "Repuesto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    repuesto.delete()
    return Response({"mensaje": "Repuesto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)


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

    serializer = ProveedorDetailSerializer(proveedores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def crear_proveedor(request):
    serializer = ProveedorCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def actualizar_proveedor(request, id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({"error": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProveedorUpdateSerializer(proveedor, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_proveedor(id):
    try:
        proveedor = Proveedor.objects.get(id=id)
    except Proveedor.DoesNotExist:
        return Response({"error": "Proveedor no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    proveedor.delete()
    return Response({"mensaje": "Proveedor eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)