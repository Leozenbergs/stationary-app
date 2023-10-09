from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    ClientSerializer,
    SellerSerializer,
    SellSerializer,
    CommitteePerWeekDaySerializer
)
from .models import (
    Product,
    Client,
    Seller,
    Sell,
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


class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer


class CommitteePerWeekDayViewSet(ModelViewSet):
    queryset = CommitteePerWeekDay.objects.all()
    serializer_class = CommitteePerWeekDaySerializer

# class StationaryAPI(APIView):
#     def get(self, request):
#         return Response({"message": "Hello, World!"})