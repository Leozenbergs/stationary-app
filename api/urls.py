from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
  ProductViewSet,
  ClientViewSet,
  SellerViewSet,
  SoldProductViewSet,
  CommitteePerWeekDayViewSet
)

api_router = DefaultRouter()
api_router.register(r'products', ProductViewSet)
api_router.register(r'clients', ClientViewSet)
api_router.register(r'sellers', SellerViewSet)
api_router.register(r'sold-product', SoldProductViewSet)
api_router.register(r'committee-per-week-day', CommitteePerWeekDayViewSet)