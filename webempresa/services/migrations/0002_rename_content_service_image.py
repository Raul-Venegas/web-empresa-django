# Generated by Django 5.0.1 on 2024-01-15 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='content',
            new_name='image',
        ),
    ]
