# Generated by Django 3.1 on 2021-04-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleh', '0004_auto_20210409_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='goodebrahim')),
            ],
        ),
    ]
