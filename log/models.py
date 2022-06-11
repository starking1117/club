from django.db import models
from django.contrib.auth.models import User

class ClubItem(models.Model):
    club_name = models.CharField('社團名稱',max_length=64,default='')
    director = models.ForeignKey(User, models.CASCADE,related_name='direct_club',name='社長')
    advisor = models.ForeignKey(User, models.CASCADE,related_name='tutor_club',name='指導老師')
    now_num = models.CharField('目前人數',max_length=8,default='')
    max_num = models.CharField('上限人數',max_length=8,default='')
    def __str__(self):
        return self.club_name

class TransferForm(models.Model):
    APPROVE_OPTIONS = [
        (0, '未答覆'), 
        (1, '同意'),
        (2, '不同意'), 
    ]
    user = models.ForeignKey(User, models.CASCADE,name='申請人',related_name='form_list')
    date_created = models.DateField('申請時間',auto_now_add=True)
    club_orig = models.ForeignKey(ClubItem, models.CASCADE,name='原社團', related_name='out_form')
    club_new = models.ForeignKey(ClubItem, models.CASCADE,name='新社團', related_name='in_form')
    approve_od = models.IntegerField('原社團社長審核', choices=APPROVE_OPTIONS, default=0)
    approve_oa = models.IntegerField('原社團指導老師審核', choices=APPROVE_OPTIONS, default=0)
    approve_nd = models.IntegerField('新社團社長審核', choices=APPROVE_OPTIONS, default=0)
    approve_na = models.IntegerField('新社團指導老師審核', choices=APPROVE_OPTIONS, default=0)
    approve_st = models.IntegerField('行政單位審核', choices=APPROVE_OPTIONS, default=0)
    note_stu = models.CharField('學生備註',max_length=255,null=True,blank=True)
    note_od = models.CharField('社長備註',max_length=255,null=True,blank=True)
    note_oa = models.CharField('指導老師備註',max_length=255,null=True,blank=True)
