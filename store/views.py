from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer

    # Below functions have been removed as directly specifying values for attributes of the class is neater
    # Such an approach can be followed in cases where we there is no special logic on top of the existing logic for serializer and queryset
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()

    # def get_serializer_class(self):
    #     return ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    # def get(self, request):
    #     queryset = Product.objects.select_related('collection').all()
    #     serializer = ProductSerializer(
    #         queryset, many=True, context={'request': request})
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     # print(serializer.validated_data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# Below is a function based view for the same product list API, which has been refactored into a class based view
# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         queryset = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(
#             queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # print(serializer.validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitems.count() > 0:
            return Response(
                {'error': 'Product cannot be deleted as it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(
            products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(products_count=Count('products')), pk=pk
    )
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response(
                {'error': 'Collection cannot be deleted as it has one or more products associated with it.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
