# Generated by Django 5.0.2 on 2024-03-06 11:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_orderitem_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)])),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier', to='store.collection')),
            ],
            options={
                'ordering': ['supplier_name'],
            },
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('arrival_date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier', to='store.supplier')),
                ('stock_in', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.supplier')),
            ],
        ),
    ]
