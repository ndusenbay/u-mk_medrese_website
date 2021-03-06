# Generated by Django 4.0.3 on 2022-04-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_bailanys'),
    ]

    operations = [
        migrations.CreateModel(
            name='dayIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=100, verbose_name='count')),
                ('date', models.CharField(max_length=100, verbose_name='date')),
            ],
            options={
                'verbose_name': 'dayIp',
                'verbose_name_plural': 'dayIps',
            },
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='Ip address')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ip',
                'verbose_name_plural': 'Ips',
            },
        ),
    ]
