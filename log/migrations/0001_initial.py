# Generated by Django 3.1.4 on 2022-06-17 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(default='', max_length=64, verbose_name='社團名稱')),
                ('now_num', models.CharField(default='', max_length=8, verbose_name='目前人數')),
                ('max_num', models.CharField(default='', max_length=8, verbose_name='上限人數')),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_club', to=settings.AUTH_USER_MODEL, verbose_name='指導老師')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direct_club', to=settings.AUTH_USER_MODEL, verbose_name='社長')),
            ],
        ),
        migrations.CreateModel(
            name='TransferForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='申請時間')),
                ('approve_od', models.IntegerField(choices=[(0, '未答覆'), (1, '同意'), (2, '不同意')], default=0, verbose_name='原社團社長審核')),
                ('approve_oa', models.IntegerField(choices=[(0, '未答覆'), (1, '同意'), (2, '不同意')], default=0, verbose_name='原社團指導老師審核')),
                ('approve_nd', models.IntegerField(choices=[(0, '未答覆'), (1, '同意'), (2, '不同意')], default=0, verbose_name='新社團社長審核')),
                ('approve_na', models.IntegerField(choices=[(0, '未答覆'), (1, '同意'), (2, '不同意')], default=0, verbose_name='新社團指導老師審核')),
                ('approve_st', models.IntegerField(choices=[(0, '未答覆'), (1, '同意'), (2, '不同意')], default=0, verbose_name='行政單位審核')),
                ('note_stu', models.CharField(blank=True, max_length=255, null=True, verbose_name='學生備註')),
                ('note_od', models.CharField(blank=True, max_length=255, null=True, verbose_name='社長備註')),
                ('note_oa', models.CharField(blank=True, max_length=255, null=True, verbose_name='指導老師備註')),
                ('club_new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_form', to='log.clubitem', verbose_name='新社團')),
                ('club_orig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='out_form', to='log.clubitem', verbose_name='原社團')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_list', to=settings.AUTH_USER_MODEL, verbose_name='申請人')),
            ],
        ),
    ]
