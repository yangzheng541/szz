# Generated by Django 4.1 on 2022-11-12 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default=0, null=True)),
                ('agree_count', models.IntegerField(default=0, null=True)),
                ('look_count', models.IntegerField(default=0, null=True)),
                ('share_count', models.IntegerField(default=0, null=True)),
                ('cover', models.ImageField(null=True, upload_to='cover', verbose_name='回答封面')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(choices=[(0, '原始状态'), (-1, '逻辑删除'), (1, '匿名')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='', null=True)),
                ('create_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('state', models.IntegerField(choices=[(0, '原始状态'), (-1, '逻辑删除'), (1, '匿名')], default=0, null=True)),
                ('fill_time', models.CharField(max_length=255, null=True)),
                ('fill_money', models.IntegerField(default=0, null=True)),
                ('type', models.IntegerField(choices=[(0, '无类型/通用类型'), (1, '其他'), (2, '心理学'), (3, '中小学教育学'), (4, '大学生'), (5, '社会调查'), (6, '产品调研'), (7, '新冠有关'), (8, '满意度调查'), (9, '测评'), (10, '考试'), (11, '网购'), (12, '就业情况'), (13, '健康')], default=0, null=True)),
                ('fill_count', models.IntegerField(default=0, null=True)),
                ('share_count', models.IntegerField(default=0, null=True)),
                ('recommend_count', models.IntegerField(default=0, null=True)),
                ('platform_type', models.IntegerField(choices=[(0, '本平台'), (1, '问卷星'), (2, '问卷网'), (3, '腾讯调查')], default=0, null=True)),
                ('platform_url', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='szz_app.questionnaire')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('questionnaire', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('required', models.BooleanField()),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('type', models.IntegerField(choices=[(0, '单选题'), (1, '多选题'), (2, '文本题')])),
                ('has_other', models.BooleanField(blank=True, null=True)),
                ('max_select', models.IntegerField(blank=True, null=True)),
                ('questionare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='szz_app.questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='', upload_to='avatar', verbose_name='头像')),
                ('sex', models.BooleanField(null=True)),
                ('birth', models.DateField(null=True)),
                ('job', models.IntegerField(choices=[(0, 'IT行业工作者'), (1, '公务员'), (2, '教师')], null=True)),
                ('address', models.CharField(default='', max_length=128, null=True)),
                ('phone', models.CharField(default='', max_length=16, null=True)),
                ('fans', models.ManyToManyField(related_name='attentions', to='szz_app.userinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_result', to='szz_app.result')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_result', to='szz_app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='TextTypeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, null=True)),
                ('topic_result', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_type_result', to='szz_app.topicresult')),
            ],
        ),
        migrations.CreateModel(
            name='TakePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('point', models.CharField(max_length=255)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='takepoints', to='szz_app.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('look_count', models.IntegerField(default=0, null=True)),
                ('share_count', models.IntegerField(default=0, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('type', models.IntegerField(choices=[(0, '无类型/通用类型'), (1, '社会热点'), (2, '心理'), (3, '文化'), (4, '影视'), (5, '音乐'), (6, '科技'), (7, '财经')], default=0, null=True)),
                ('state', models.IntegerField(choices=[(0, '原始状态'), (-1, '逻辑删除'), (1, '匿名')], default=0, null=True)),
                ('cover', models.ImageField(null=True, upload_to='cover', verbose_name='问题封面')),
                ('questionnaires', models.ManyToManyField(related_name='questions', to='szz_app.questionnaire')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='picture', verbose_name='任意图片')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OptionTypeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(blank=True, null=True)),
                ('topic_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_type_result', to='szz_app.topicresult')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.IntegerField()),
                ('content', models.TextField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='szz_app.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('data', models.TextField()),
                ('takepoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='szz_app.takepoint')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='szz_app.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
    ]
