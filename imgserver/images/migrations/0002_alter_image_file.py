# Generated by Django 4.1.5 on 2023-01-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]
