# Generated by Django 3.0.5 on 2020-12-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneinc', '0002_auto_20201223_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getinfo',
            old_name='responseCode',
            new_name='responseMessage',
        ),
        migrations.AddField(
            model_name='getinfo',
            name='ResponseCode',
            field=models.CharField(default='', max_length=100),
        ),
    ]
