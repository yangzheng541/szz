# Generated by Django 4.1 on 2022-09-22 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szz_app', '0013_answer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='question1',
        ),
    ]
