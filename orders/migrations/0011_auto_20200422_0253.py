# Generated by Django 2.0.12 on 2020-04-22 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200422_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='num_of_topings',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping1',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping2',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping3',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='topping4',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]