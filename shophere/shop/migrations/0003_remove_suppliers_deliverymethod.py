# Generated by Django 2.2 on 2019-05-12 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190512_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suppliers',
            name='deliveryMethod',
        ),
    ]
