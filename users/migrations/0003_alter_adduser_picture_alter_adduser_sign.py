# Generated by Django 4.1.2 on 2022-10-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_adduser_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='adduser',
            name='sign',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
