from rest_framework.serializers import ModelSerializer
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import Product
from .documents import ProductDocument

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ElasticProductSerializer(DocumentSerializer):
    class Meta:
        model = Product
        document = ProductDocument
        fields = '__all__'