# Generated by Django 4.2.8 on 2023-12-25 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantapp', '0006_alter_userregister_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='full_name',
            new_name='name',
        ),
    ]
