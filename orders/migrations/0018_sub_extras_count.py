# Generated by Django 2.0.12 on 2020-04-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20200424_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='extras_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]