# Generated by Django 4.1 on 2022-09-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='fill_time',
            field=models.DateTimeField(null=True),
        ),
    ]
