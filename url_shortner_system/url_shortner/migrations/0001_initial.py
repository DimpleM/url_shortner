# Generated by Django 3.0.8 on 2020-08-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLs',
            fields=[
                ('expiry_time', models.DateTimeField(blank=True, null=True)),
                ('shortURL', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('targetURL', models.CharField(max_length=2083)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('private_token', models.CharField(blank=True, max_length=200)),
                ('click_info', models.IntegerField(default=1)),
            ],
        ),
    ]