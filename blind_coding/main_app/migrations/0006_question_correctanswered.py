# Generated by Django 2.0.13 on 2019-03-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_userdata_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correctAnswered',
            field=models.IntegerField(default=0),
        ),
    ]
