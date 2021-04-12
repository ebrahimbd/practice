# Generated by Django 3.1 on 2021-04-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleh', '0019_auto_20210411_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=30)),
            ],
        ),
    ]
