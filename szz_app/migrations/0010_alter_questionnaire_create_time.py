# Generated by Django 4.1 on 2022-09-21 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szz_app', '0009_alter_questionnaire_fill_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
