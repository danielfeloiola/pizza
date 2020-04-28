# Generated by Django 2.0.12 on 2020-04-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20200422_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('num_of_topings', models.IntegerField()),
                ('topping1', models.CharField(max_length=64)),
                ('topping2', models.CharField(max_length=64)),
                ('topping3', models.CharField(max_length=64)),
                ('topping4', models.CharField(max_length=64)),
                ('extra_cheese', models.BooleanField()),
                ('extra_green_pepper', models.BooleanField()),
                ('extra_mushroom', models.BooleanField()),
                ('extra_onion', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(blank=True, to='orders.CartItem'),
        ),
    ]
