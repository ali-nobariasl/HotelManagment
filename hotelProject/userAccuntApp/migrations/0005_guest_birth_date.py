# Generated by Django 4.2.6 on 2023-10-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccuntApp', '0004_alter_guest_checkin_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]