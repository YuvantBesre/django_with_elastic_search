from rest_framework.serializers import ModelSerializer
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import Product
from .documents import ProductDocument

# PRODUCT SERIALIZER FOR CREATION, EDIT
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# PRODUCT SERIALIZER FOR LIST AND SEARCH
class ElasticProductSerializer(DocumentSerializer):
    class Meta:
        model = Product
        document = ProductDocument
        fields = ['id', 'name', 'price', 'quantity', 'created', 'modified']

        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}