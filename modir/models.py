from operator import mod
from django.db import models


class Letter(models.Model):
    subtitle = models.CharField(max_length=20,default='نامه',verbose_name='عنوان نامه')
    discription = models.CharField(max_length=100 , verbose_name='توضیحات',default='توضیح')
    positionlist = [('choice','انتخاب کنید'),
                ('ath-admin','مدیر اتوماسیون-رییس هییت مدیر'),
                ('ath-dabir','مدیر اتوماسیون-دبیر کل'),
                ('ath-karpardaz','مدیر اتوماسیون-کارپرداز و پیک'),
                ('ath-graphic','مدیر اتوماسیون-واحد گرافیک'),
                ('ath-dabirmarkazi','مدیر اتوماسیون-کارشناس دبیرخانه مرکزی'),
                ('ath-boss','مدیر اتوماسیون-رییس'),]
    position = models.CharField(max_length=20 , choices=positionlist , null=True)


    signatory = models.CharField(max_length= 50 ,null=True,choices=[('db-main','دبیرخانه مرکزی'),
    ('db-heiat','کاربر دبیرخانه-ریس هیات امنا'),('nboss-heiat','نایب رییس هیات امنا')
    ,('boss-autoheiat','مدیر اتوماسیون-رییس هیات مدیره'),('khazane','خزانه دار'),
    ('ath-dabirkol','مدیر اتوماسیون-دبیر کل'),('boss-excute','مدیر اجرایی')
    ,('boss-dokhaniat','رییس مرکز تحقیقات کنترل دخانیات'),('nboss-hmodir','نایب رییس هیت مدیره')
    ,('db-hamayesh','دبیر کل همایش'),('boss-ath-dbmain','مدیر اتوماسیون -کارشناس دبیرخانه مرکزی')
    ,('test','تست'),])

    secretariat = models.CharField(max_length=50 , null=True , choices=[('markaz_tahghigh','دبیرخانه مرکز تحقیقات'),
    ('hamayesh','دبیرخانه همایش')])

    receivers = models.CharField(max_length=50, null=True, choices=[('test','test'),
    ('test2','test2'),('test3','test3'),('test3','test3'),('test3','test3'),('test3','test3')])


    Transcript = models.CharField(max_length=50, null=True, choices=[('test','test'),('test2','test2'),('test3','test3'),('test3','test3'),('test3','test3'),('test3','test3')])

    ready_text = models.CharField(max_length=50, null=True, choices=[('test','test')])

    size_letter = models.CharField(max_length=50, null=True, choices=[('A4','A4'),('A5','A5')])

