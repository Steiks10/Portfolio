# Generated by Django 5.0.6 on 2024-06-21 18:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
