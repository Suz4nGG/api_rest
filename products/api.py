from products.models import Products
from rest_framework import viewsets, permissions
from products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Products.objects.all()
  permissions_classes = [permissions.AllowAny]
  serializer_class = ProductSerializer