# Generated by Django 3.1.7 on 2021-02-24 18:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_by', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ('order_by',),
            },
        ),
    ]
