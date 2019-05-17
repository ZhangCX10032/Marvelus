# Generated by Django 2.2.1 on 2019-05-17 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventCenter', '0008_auto_20190517_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
