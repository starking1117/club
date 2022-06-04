# Generated by Django 3.1.4 on 2022-06-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_delete_clubitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(default='', max_length=8, verbose_name='社團名稱')),
                ('director', models.CharField(max_length=8, verbose_name='社長')),
                ('teacher', models.CharField(max_length=8, verbose_name='指導老師')),
                ('now_num', models.CharField(max_length=8, verbose_name='目前人數')),
                ('max_num', models.CharField(max_length=8, verbose_name='上限人數')),
            ],
        ),
    ]
