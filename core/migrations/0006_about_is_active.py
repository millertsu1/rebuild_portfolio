# Generated by Django 5.1 on 2024-08-22 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_about_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
