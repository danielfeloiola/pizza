# Generated by Django 2.0.12 on 2020-04-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0028_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='hour',
            name='msg',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
