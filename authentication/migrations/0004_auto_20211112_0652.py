# Generated by Django 3.2.9 on 2021-11-12 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20211112_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]