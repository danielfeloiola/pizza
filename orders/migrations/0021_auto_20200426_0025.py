# Generated by Django 2.0.12 on 2020-04-26 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20200425_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='extra_cheese',
            new_name='extra_1',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='extra_green_pepper',
            new_name='extra_2',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='extra_mushroom',
            new_name='extra_3',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='extra_onion',
            new_name='extra_4',
        ),
    ]
