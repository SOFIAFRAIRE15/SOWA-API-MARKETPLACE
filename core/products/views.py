from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProductSerializer

from .models import Product


# Create your views here.

def index_product(request):
    return JsonResponse({"message" : "Online" })


class ProductView(APIView):
    def get(self, request, pk = None):
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product)

        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   