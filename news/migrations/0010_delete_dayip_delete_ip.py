# Generated by Django 4.0.3 on 2022-04-18 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_remove_ip_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='dayIp',
        ),
        migrations.DeleteModel(
            name='Ip',
        ),
    ]
