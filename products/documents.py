from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
    
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 1
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

# PUBLISHER_INDEX = Index('products')

# PUBLISHER_INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=1
# )

# @PUBLISHER_INDEX.doc_type
# class ProductDocument(Document):
    
#     id = fields.IntegerField(attr='id')
#     fielddata=True
#     name = fields.TextField(
#         fields={
#             'raw':{
#                 'type': 'text',
#             }
#         }
#     )
#     price = fields.FloatField(
#         fields = {
#             'raw':{
#                 'type': 'float',
#             }
#         }
#     ),
#     quantity = fields.IntegerField(
#         fields = {
#             'raw' : {
#                 'type' : 'integer'
#             }
#         }
#     )
#     created = fields.DateField(
#         fields = {
#             'raw' : {
#                 'type' : 'text'
#             }
#         }
#     )
    
   
#     class Django(object):
#         model = Product