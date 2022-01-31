from django.core.management.base import BaseCommand
from products.models import Product

products = [
    {
        'name' : 'Needle Holder',
        'price' : 478.01,
        'quantity' : 500
    },
    {
        'name' : 'Absorbent Cotton',
        'price' : 56.4,
        'quantity' : 50
    },
    {
        'name' : 'Ensure Diabetes care jar',
        'price' : 696,
        'quantity' : 55
    },
    {
        'name' : 'Urine Pot (Female)',
        'price' : 112,
        'quantity' : 10
    },
    {
        'name' : 'Blood Pressure cuff (Adult)',
        'price' : 420.5,
        'quantity' : 10
    },
    {
        'name' : 'BP Bulb',
        'price' : 134.01,
        'quantity' : 25
    },
    {
        'name' : 'Heating Pad Gel',
        'price' : 402,
        'quantity' : 6
    },
    {
        'name' : 'Ethilon 2.0 Suture',
        'price' : 194.36,
        'quantity' : 1
    },
    {
        'name' : 'Neocan (24G)',
        'price' : 107.2,
        'quantity' : 1
    },
]

# COMMAND TO CREATE PRODUCT INSTANCES
class Command(BaseCommand):
    help = 'Create Products'
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        for product in products:
            Product.objects.create(
                name = product['name'],
                price = product['price'],
                quantity = product['quantity']
            )
            self.stdout.write('.')
        self.stdout.write("Products Created Successfully!")