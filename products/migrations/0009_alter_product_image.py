# Generated by Django 3.2 on 2021-04-08 02:12

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210408_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/default.jpg', upload_to=products.models.uploadTo),
        ),
    ]
