# Generated by Django 2.2.1 on 2019-06-10 16:10

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('definitions', '0003_term_and_definition_inherit_from_base_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('value',)),
        ),
    ]
