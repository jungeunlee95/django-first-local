# Generated by Django 2.1.7 on 2019-03-12 14:30

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='posting/resize/%Y%m%d'),
        ),
    ]
