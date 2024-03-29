# Generated by Django 4.1.3 on 2022-11-27 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modir', '0002_alter_root_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DabirKhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('harfVarede', models.CharField(max_length=100)),
                ('harfShomareDakheli', models.CharField(max_length=100)),
                ('harfShomareSadere', models.CharField(max_length=100)),
                ('shomareNameAghazin', models.CharField(max_length=100)),
                ('choiceDabirKhone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modir.root')),
            ],
        ),
    ]
