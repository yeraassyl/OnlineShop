# Generated by Django 2.2 on 2019-05-12 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_transactions_isorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='supId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Suppliers'),
        ),
    ]
