# Generated by Django 5.0.3 on 2024-03-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_ourwork_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutvideo',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
