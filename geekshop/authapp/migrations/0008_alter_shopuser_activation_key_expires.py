# Generated by Django 4.0 on 2022-01-28 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_shopuser_activation_key_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 30, 14, 22, 50, 626866)),
        ),
    ]