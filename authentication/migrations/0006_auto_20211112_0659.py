# Generated by Django 3.2.9 on 2021-11-12 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20211112_0654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
