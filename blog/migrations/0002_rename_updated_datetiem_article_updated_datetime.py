# Generated by Django 3.2.7 on 2021-09-03 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='updated_datetiem',
            new_name='updated_datetime',
        ),
    ]
