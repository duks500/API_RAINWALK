# Generated by Django 3.0.5 on 2020-12-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneinc', '0006_auto_20201227_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getinfo',
            name='PortalOneSessionKey',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
