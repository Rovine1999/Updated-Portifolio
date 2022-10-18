# Generated by Django 3.1.7 on 2021-08-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=500, null=True)),
                ('message', models.TextField(blank=True, max_length=5000, null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]