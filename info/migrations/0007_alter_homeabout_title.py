# Generated by Django 5.0.3 on 2024-03-12 23:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_rename_maps_link_contactinfo_map_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeabout',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
