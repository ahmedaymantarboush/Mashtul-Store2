# Generated by Django 3.1.7 on 2021-04-08 01:58

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210408_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=products.models.uploadTo),
        ),
    ]
