from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductListCreate.as_view()),
    path('products/<int:pk>', views.ProductRetrieveUpdate.as_view())
] 