# Generated by Django 4.1.5 on 2023-01-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]