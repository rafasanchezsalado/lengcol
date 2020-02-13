# Generated by Django 2.2.1 on 2019-06-05 20:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0002_term_value_is_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='definition',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='definition',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='term',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
