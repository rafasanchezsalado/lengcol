# Generated by Django 2.2.2 on 2019-06-25 21:55

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0006_definition_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='definition',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
