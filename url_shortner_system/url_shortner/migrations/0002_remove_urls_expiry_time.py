# Generated by Django 3.0.8 on 2020-08-01 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urls',
            name='expiry_time',
        ),
    ]