# Generated by Django 2.0.12 on 2020-04-22 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200422_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.CartItem'),
        ),
    ]