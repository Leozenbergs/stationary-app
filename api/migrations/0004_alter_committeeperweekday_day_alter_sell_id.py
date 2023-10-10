# Generated by Django 4.2.4 on 2023-10-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_sell_sold_products_soldproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeeperweekday',
            name='day',
            field=models.IntegerField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1),
        ),
        migrations.AlterField(
            model_name='sell',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
