# Generated by Django 3.2 on 2021-05-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210505_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='user',
            new_name='owner',
        ),
    ]