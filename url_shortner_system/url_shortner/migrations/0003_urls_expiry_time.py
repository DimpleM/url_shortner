# Generated by Django 3.0.8 on 2020-08-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0002_remove_urls_expiry_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='expiry_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
