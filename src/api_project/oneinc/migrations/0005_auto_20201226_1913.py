# Generated by Django 3.0.5 on 2020-12-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oneinc', '0004_auto_20201225_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getinfo',
            old_name='PortalOneSessionKey',
            new_name='portalOneSessionKey',
        ),
        migrations.RenameField(
            model_name='getinfo',
            old_name='ResponseCode',
            new_name='responseCode',
        ),
        migrations.RenameField(
            model_name='getinfo',
            old_name='ResponseMessage',
            new_name='responseMessage',
        ),
    ]