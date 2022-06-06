# Generated by Django 4.0.3 on 2022-03-19 10:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_studentbest_text_studentbest_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='medreseTecher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fullName', models.CharField(max_length=100000)),
                ('photo', models.ImageField(blank=True, default=0, null=True, upload_to='medreseTecher_media')),
                ('field_name', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ұстаз',
                'verbose_name_plural': 'Ұстаздар',
            },
        ),
    ]
