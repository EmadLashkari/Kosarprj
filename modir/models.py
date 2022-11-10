from operator import mod
from django.db import models


class Level(models.Model):
    name = models.CharField(max_length = 51)
    nameplz = models.CharField(max_length = 51)
    sign = models.BooleanField()
    parentID = models.IntegerField()

    def __str__(self):
        return self.name

class Letter(models.Model):
    subtitle = models.CharField(max_length=20,verbose_name='عنوان نامه')
    discription = models.CharField(max_length=100 , verbose_name='توضیحات')
    position = models.ForeignKey(Level , on_delete = models.CASCADE, related_name ='position')
    signatory = models.ForeignKey(Level , on_delete = models.CASCADE , related_name = 'signatory' )
    secretariat = models.ForeignKey(Level , on_delete = models.CASCADE, related_name ='secretariat')
    receivers = models.ForeignKey(Level , on_delete = models.CASCADE, related_name ='receivers')
    Transcript = models.ForeignKey(Level , on_delete = models.CASCADE, related_name ='Transcript')
    ready_text = models.CharField(max_length=50, choices=[('test','test')])
    size_letter = models.CharField(max_length=50, choices=[('A4','A4'),('A5','A5')])

    def __str__(self):
        return self.subtitle