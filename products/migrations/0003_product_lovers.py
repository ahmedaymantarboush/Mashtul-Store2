# Generated by Django 3.1.7 on 2021-04-05 23:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20210406_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lovers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
