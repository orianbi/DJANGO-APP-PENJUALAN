# Generated by Django 3.2 on 2021-04-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='custemer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.custemer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.product'),
        ),
    ]
