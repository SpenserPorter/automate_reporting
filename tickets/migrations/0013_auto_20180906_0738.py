# Generated by Django 2.1 on 2018-09-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20180830_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_large_response_time',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_negative_response_time',
            field=models.BooleanField(default=False),
        ),
    ]
