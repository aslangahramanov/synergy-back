# Generated by Django 5.0.3 on 2024-03-12 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_aboutvideo_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactinfo',
            old_name='adress',
            new_name='address',
        ),
    ]
