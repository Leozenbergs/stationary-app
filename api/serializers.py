from rest_framework.serializers import ModelSerializer
from .models import (
  Product,
  Client,
  Seller,
  Sell
)

class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = ('code', 'description', 'price', 'comittee')

class ClientSerializer(ModelSerializer):
  class Meta:
    model = Client
    fields = ('id', 'name', 'email', 'phone')

class SellerSerializer(ModelSerializer):
  class Meta:
    model = Seller
    fields = ('id', 'name', 'email', 'phone')


class SellSerializer(ModelSerializer):
  class Meta:
    model = Sell
    fields = ('note_code', 'client', 'seller', 'sold_products', 'date')