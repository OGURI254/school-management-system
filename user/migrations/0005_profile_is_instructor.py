# Generated by Django 5.0.1 on 2024-03-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
