# Generated by Django 4.2.6 on 2023-10-05 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userAccuntApp', '0005_guest_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='checkin_date',
        ),
    ]
