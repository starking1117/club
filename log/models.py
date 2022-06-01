from django.db import models

# Create your models here.
class Student(models.Model):
    studata = models.TextField('學生資料', help_text='依 班級,座號,學號,身分證字號,姓名 順序由 Excel 貼上學生基本資料')

class LogItem(models.Model):
    student = models.CharField('',max_length=255)

