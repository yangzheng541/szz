# Generated by Django 4.1 on 2022-09-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szz_app', '0007_time_alter_questionnaire_fill_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='fill_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
