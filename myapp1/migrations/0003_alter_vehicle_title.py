# Generated by Django 3.2.9 on 2021-12-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_brand_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]