# Generated by Django 4.1.3 on 2022-12-01 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0005_alter_dabirkhone_choicedabirkhone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='secretariat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretariat', to='modir.dabirkhone'),
        ),
    ]
