# Generated by Django 5.0.3 on 2024-03-14 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('title',)},
        ),
    ]