from django.contrib import admin
from .models import (
  Product,
  Seller,
  Client,
  Sell
)

# Register your models here.
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(Client)
admin.site.register(Sell)