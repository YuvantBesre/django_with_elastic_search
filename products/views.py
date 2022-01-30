from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from .serializers import ProductSerializer, ElasticProductSerializer
from .models import Product
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend, OrderingFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ProductDocument
from rest_framework.pagination import PageNumberPagination

class ProductList(DocumentViewSet):
    document = ProductDocument
    serializer_class = ElasticProductSerializer
    filter_backends = [FilteringFilterBackend, OrderingFilterBackend, CompoundSearchFilterBackend]
    search_fields = ['name']
    multi_match_search_fields = ['name']
    filter_fields = {
        'name' : 'name',
        'quantity' : 'quantity'
    }
    ordering_fields = {
        'created' : 'created',
        'quantity' : 'quantity'
    }
    ordering = ('id',)
    pagination_class = PageNumberPagination

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
