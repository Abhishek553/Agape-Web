# Generated by Django 3.0.7 on 2020-09-06 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200906_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_id',
            new_name='id',
        ),
    ]