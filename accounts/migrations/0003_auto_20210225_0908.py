# Generated by Django 3.1.6 on 2021-02-25 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_password2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password1',
            new_name='password',
        ),
    ]
