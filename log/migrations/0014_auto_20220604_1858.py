# Generated by Django 3.1.4 on 2022-06-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0013_clubitem_stu_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubitem',
            name='stu_name',
        ),
        migrations.AlterField(
            model_name='clubitem',
            name='club_name',
            field=models.CharField(default='', max_length=8, verbose_name='社團名稱'),
        ),
        migrations.AlterField(
            model_name='clubitem',
            name='director',
            field=models.CharField(default='', max_length=8, verbose_name='社長'),
        ),
        migrations.AlterField(
            model_name='clubitem',
            name='max_num',
            field=models.CharField(default='', max_length=8, verbose_name='上限人數'),
        ),
        migrations.AlterField(
            model_name='clubitem',
            name='now_num',
            field=models.CharField(default='', max_length=8, verbose_name='目前人數'),
        ),
        migrations.AlterField(
            model_name='clubitem',
            name='teacher',
            field=models.CharField(default='', max_length=8, verbose_name='指導老師'),
        ),
        migrations.AlterField(
            model_name='formitem',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='formitem',
            name='stu_name',
            field=models.CharField(default='', max_length=8, verbose_name='學生姓名'),
        ),
        migrations.AlterField(
            model_name='formitem',
            name='stu_num',
            field=models.CharField(default='', max_length=8, verbose_name='座號'),
        ),
    ]
