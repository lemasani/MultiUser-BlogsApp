# Generated by Django 5.1 on 2024-09-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
    ]
