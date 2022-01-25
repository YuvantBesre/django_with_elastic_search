from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view({'get': 'list'})),
    path('product/create/', views.ProductCreate.as_view()),
    path('products/<int:pk>', views.ProductRetrieveUpdate.as_view())
] 