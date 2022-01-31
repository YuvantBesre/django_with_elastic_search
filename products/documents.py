from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Product

# DOCUMENT FOR ELASTIC SEARCH
@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
    
    settings = {
        'number_of_shards': 1, # Shards are the division of the index so that the large amount of data can be distributed and managed.
        'number_of_replicas': 1 # Replicas are the copy of shards in case of any failure replicas help
    }

    fielddata = True

    name = fields.TextField(
        fields = {
            'raw' : {
                'type': 'text',
            }
        }
    ) 

    class Django:
        model = Product         
        fields = [
            'id',
            'quantity',
            'price',
            'created',
            'modified'
        ]
