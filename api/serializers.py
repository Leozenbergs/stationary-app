import calendar
from datetime import datetime

from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import (
  Product,
  Client,
  Seller,
  CommitteePerWeekDay,
  SoldProduct
)


class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = ('code', 'description', 'price', 'committee')

class ClientSerializer(ModelSerializer):
  class Meta:
    model = Client
    fields = ('id', 'name', 'email', 'phone')

class SellerSerializer(ModelSerializer):
  class Meta:
    model = Seller
    fields = ('id', 'name', 'email', 'phone')

class SoldProductSerializer(ModelSerializer):
  def create(self, validated_data):
    current_day = datetime.now().isoweekday()
    day_of_week = calendar.day_name[current_day - 1].upper()
    has_limit = CommitteePerWeekDay.objects.filter(day=day_of_week).first()
    product = Product.objects.get(description=validated_data['product'])

    if (has_limit):
      if (day_of_week == has_limit.day):
        if (product.committee >= has_limit.max_committee):
          product.update(committee=has_limit.max_committee)
        elif (product.committee <= has_limit.min_committee):
          product.update(committee=has_limit.min_committee)

    return SoldProduct.objects.create(
      sell=validated_data['sell'],
      product=validated_data['product']
    )
  class Meta:
    model = SoldProduct
    fields = ('id', 'sell', 'product')

class CommitteePerWeekDaySerializer(ModelSerializer):
  class Meta:
    model = CommitteePerWeekDay
    fields = ('day', 'min_committee', 'max_committee')