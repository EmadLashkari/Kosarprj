# Generated by Django 4.1.2 on 2022-10-29 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_adduser_picture_alter_adduser_sign'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddUser',
        ),
    ]