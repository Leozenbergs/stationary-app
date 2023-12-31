from django.db import models

DAY_OF_THE_WEEK = (
  ('1', 'Monday'),
  ('2', 'Tuesday'),
  ('3', 'Wednesday'),
  ('4', 'Thursday'),
  ('5', 'Friday'),
  ('6', 'Saturday'), 
  ('7', 'Sunday'),
)

# Create your models here.
class Product(models.Model):
  code = models.AutoField(primary_key=True)
  description = models.CharField(max_length=200)
  price = models.FloatField()
  committee = models.IntegerField(choices=((i,i) for i in range(1, 10)))



class Client(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)

class Seller(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)

# Uma venda tem número da nota fiscal, data/hora, cliente, vendedor e uma lista de um ou mais produtos e suas quantidades vendidas.
class Sell(models.Model):
  note_code = models.CharField(max_length=200)
  client = models.ForeignKey(Client, verbose_name=("client"), on_delete=models.CASCADE)
  seller = models.ForeignKey(Seller, verbose_name=("seller"), on_delete=models.CASCADE)
  sold_products = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

class CommitteePerWeekDay(models.Model):
  day = models.CharField(max_length=1, choices=DAY_OF_THE_WEEK)
  min_committee = models.IntegerField(choices=((i,i) for i in range(1, 10)))
  max_committee = models.IntegerField(choices=((i,i) for i in range(1, 10)))