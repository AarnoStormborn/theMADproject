# Generated by Django 4.0.6 on 2022-10-26 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_profile_isseller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='isSeller',
        ),
    ]
