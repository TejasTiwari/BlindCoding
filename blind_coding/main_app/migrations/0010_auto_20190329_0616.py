# Generated by Django 2.0.13 on 2019-03-29 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20190329_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='answer',
            new_name='answerGiven',
        ),
    ]
