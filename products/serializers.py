from rest_framework import serializers
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = ("id","precio", "tipo", "marca", "nombre", "creacion")
    read_only_fields = ("creacion",)