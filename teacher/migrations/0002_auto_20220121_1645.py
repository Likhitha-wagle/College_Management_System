# Generated by Django 3.2.5 on 2022-01-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='classid',
        ),
        migrations.AddField(
            model_name='teacher',
            name='classid',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
