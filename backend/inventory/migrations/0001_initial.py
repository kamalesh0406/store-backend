# Generated by Django 4.0.1 on 2022-01-16 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('date', models.DateField()),
                ('destination', models.CharField(max_length=120)),
                ('number_products', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.shipment')),
            ],
        ),
    ]
