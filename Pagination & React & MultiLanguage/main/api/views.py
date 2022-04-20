from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from main import models


@api_view(['GET'])
def RoutesView(request):
    """All API routes"""
    routes = [
        'GET /api/',
        'GET /api/products/',
        'GET /api/product/:id/',
    ]
    return Response(routes)


@api_view(['GET'])
def ProductsView(request):
    """All products"""
    products = models.Product.objects.all()
    serializer = serializers.ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProductView(request, pk):
    """Get product by id"""
    product = models.Product.objects.get(id=pk)
    serializer = serializers.ProductSerializer(product, many=False)
    return Response(serializer.data)
