# Generated by Django 3.0.5 on 2020-12-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneinc', '0002_getinfo_customerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getinfo',
            name='CustomerId',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getinfo',
            name='CustomerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getinfo',
            name='ExternalCustomerId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getinfo',
            name='PortalOneSessionKey',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getinfo',
            name='ResponseCode',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getinfo',
            name='ResponseMessage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
