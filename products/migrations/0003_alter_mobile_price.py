# Generated by Django 4.0.6 on 2022-10-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_mobile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.PositiveBigIntegerField(),
        ),
    ]