# Generated by Django 4.0.4 on 2022-04-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_creator', '0002_endpoint_validate_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_identifier',
            field=models.CharField(max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
