# Generated by Django 5.0.1 on 2024-03-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_uploadmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
