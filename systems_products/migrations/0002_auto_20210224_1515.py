# Generated by Django 3.1.7 on 2021-02-24 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systems_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemsproduct',
            options={'ordering': ('order_by',), 'verbose_name': 'Systems Product', 'verbose_name_plural': 'Systems Products'},
        ),
    ]
