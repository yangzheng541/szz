# Generated by Django 4.1 on 2022-09-23 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szz_app', '0019_alter_optionresult_topic_alter_textresult_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='answer',
        ),
    ]
