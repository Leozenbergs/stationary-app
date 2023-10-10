from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
import calendar
from .serializers import (
    ProductSerializer,
    ClientSerializer,
    SellerSerializer,
    SoldProductSerializer,
    CommitteePerWeekDaySerializer
)
from .models import (
    Product,
    Client,
    Seller,
    SoldProduct,
    CommitteePerWeekDay
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SoldProductViewSet(ModelViewSet):
    queryset = SoldProduct.objects.all()
    serializer_class = SoldProductSerializer


class CommitteePerWeekDayViewSet(ModelViewSet):
    queryset = CommitteePerWeekDay.objects.all()
    serializer_class = CommitteePerWeekDaySerializer
