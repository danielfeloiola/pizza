# Generated by Django 2.0.12 on 2020-04-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_sub_extras_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='extras_count',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='sub_extras_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]