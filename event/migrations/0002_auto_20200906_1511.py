# Generated by Django 3.0.7 on 2020-09-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(upload_to='static/images/upload'),
        ),
    ]
