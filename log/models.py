from django.db import models

class FormItem(models.Model):
    GRADE_OPTIONS = [
    (0, '高一'),
    (1, '高二'),
    ]
    CLASS_OPTIONS = [
    (0, '1'),
    (1, '2'),
    (2, '3'),
    (3, '4'),
    (4, '5'),
    (5, '6'),
    (6, '7'),
    (7, '8'),
    (8, '9'),
    (9, '10'),
    ] 
    CLUB_OPTIONS = [
    (0, '資訊社'), 
    (1, '籃球社'), 
    (2, '羽球社'),
    (3, '桌遊社'),
    (4, '吉他社'),
    ]
    stu_name = models.CharField('學生姓名', max_length=8,default='')
    stu_grade = models.IntegerField(
            '年級', 
            default=0, 
            choices=GRADE_OPTIONS
           )
    #學生班級
    stu_class = models.IntegerField(
            '學生班級', 
            default=0, 
            choices=CLASS_OPTIONS
           )
    stu_num = models.CharField('座號', max_length=8,default='')
    ori_club = models.IntegerField(
            '原社團', 
            default=0, 
            choices=CLUB_OPTIONS 
    )
    new_club = models.IntegerField(
            '欲轉社社團', 
            default=0, 
            choices=CLUB_OPTIONS 
    )
    Yes_or_No = models.BooleanField('同意轉社',default=False)
    note = models.CharField('備註',max_length=255,null= True,blank= True)


class ClubItem(models.Model):
    club_name = models.CharField('社團名稱',max_length=8,default='')
    director = models.CharField('社長', max_length=8,default='')
    teacher = models.CharField('指導老師', max_length=8,default='')
    now_num = models.CharField('目前人數',max_length=8,default='')
    max_num = models.CharField('上限人數',max_length=8,default='')