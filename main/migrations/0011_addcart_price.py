# Generated by Django 4.0.4 on 2022-04-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_addcart_price_addcart_single_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcart',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
