# Generated by Django 3.1.7 on 2021-08-18 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='title',
        ),
    ]
