# Generated by Django 2.1 on 2018-08-28 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20180828_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ticket_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Agent')),
            ],
        ),
    ]
