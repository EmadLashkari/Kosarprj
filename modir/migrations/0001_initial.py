# Generated by Django 4.0.6 on 2022-09-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('choice', 'انتخاب کنید'), ('ath-admin', 'مدیر اتوماسیون-رییس هییت مدیر'), ('ath-dabir', 'مدیر اتوماسیون-دبیر کل'), ('ath-karpardaz', 'مدیر اتوماسیون-کارپرداز و پیک'), ('ath-graphic', 'مدیر اتوماسیون-واحد گرافیک'), ('ath-dabirmarkazi', 'مدیر اتوماسیون-کارشناس دبیرخانه مرکزی'), ('ath-boss', 'مدیر اتوماسیون-رییس')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.ManyToManyField(to='modir.position')),
            ],
        ),
    ]
