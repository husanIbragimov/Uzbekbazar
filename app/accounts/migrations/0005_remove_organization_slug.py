# Generated by Django 5.0 on 2024-08-16 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_organization_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='slug',
        ),
    ]
