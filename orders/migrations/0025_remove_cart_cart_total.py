# Generated by Django 2.0.12 on 2020-04-26 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20200426_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_total',
        ),
    ]
