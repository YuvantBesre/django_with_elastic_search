from django.db import models

# PRODUCT MODULE
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        
    def __str__(self):
        return self.name
    
