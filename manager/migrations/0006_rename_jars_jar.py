# Generated by Django 5.0.4 on 2024-04-30 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_jars_file_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jars',
            new_name='jar',
        ),
    ]