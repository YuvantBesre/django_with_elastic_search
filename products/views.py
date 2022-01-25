from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import ProductSerializer, ElasticProductSerializer
from .models import Product
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend, OrderingFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ProductDocument


class ProductList(DocumentViewSet):
    document = ProductDocument
    serializer_class = ElasticProductSerializer
    filter_backends = [ FilteringFilterBackend, OrderingFilterBackend, CompoundSearchFilterBackend,]
    search_fields = ['name', 'price']
    multi_match_search_fields = ['name', 'quantity', 'price']
    filter_fields = {
        'name' : 'name',
        'price' : 'price',
        'quantity' : 'quantity'
    }
    ordering_fields = {
        'price' : 'price',
        'quantity' : 'quantity'
    }

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
