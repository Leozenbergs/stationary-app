from django.db import models

DAY_OF_THE_WEEK = (
    ('MONDAY', 'Monday'),
    ('TUESDAY', 'Tuesday'),
    ('WEDNESDAY', 'Wednesday'),
    ('THURSDAY', 'Thursday'),
    ('FRIDAY', 'Friday'),
    ('SATURDAY', 'Saturday'),
    ('SUNDAY', 'Sunday'),
)


class Product(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    committee = models.IntegerField(choices=((i, i) for i in range(1, 10)))

    def __str__(self):
        return self.description


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sell(models.Model):
    id = models.AutoField(primary_key=True)
    note_code = models.CharField(max_length=200)
    client = models.ForeignKey(Client, verbose_name=("client"), on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, verbose_name=("seller"), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note_code


class SoldProduct(models.Model):
    id = models.AutoField(primary_key=True)
    sell = models.ForeignKey(Sell, verbose_name=("sell"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("product"), on_delete=models.CASCADE)

    def __str__(self):
        return self.sell.note_code


class CommitteePerWeekDay(models.Model):
    day = models.CharField(max_length=200, choices=DAY_OF_THE_WEEK)
    min_committee = models.IntegerField(choices=((i, i) for i in range(1, 10)))
    max_committee = models.IntegerField(choices=((i, i) for i in range(1, 10)))

    def __str__(self):
        return f"{self.day} min={self.min_committee}% max={self.max_committee}%"
