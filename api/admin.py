from django.contrib import admin
from .models import (
  Product,
  Seller,
  Client,
  Sell,
  SoldProduct,
  CommitteePerWeekDay
)

# Register your models here.
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Client)
admin.site.register(Sell)
admin.site.register(SoldProduct)
admin.site.register(CommitteePerWeekDay)