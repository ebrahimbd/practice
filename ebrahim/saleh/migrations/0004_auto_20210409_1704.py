# Generated by Django 3.1 on 2021-04-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleh', '0003_auto_20210409_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleh',
            name='image',
            field=models.ImageField(blank=True, upload_to='goodebrahim'),
        ),
    ]
