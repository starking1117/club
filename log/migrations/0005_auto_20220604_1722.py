# Generated by Django 3.1.4 on 2022-06-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20220604_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubitem',
            name='club_name',
            field=models.CharField(default='', max_length=8, verbose_name='社團名稱'),
        ),
    ]
