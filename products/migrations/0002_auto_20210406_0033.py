# Generated by Django 3.1.7 on 2021-04-05 22:33

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=products.models.uploadTo),
        ),
    ]
