# Generated by Django 3.0 on 2019-12-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KakaoAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_id', models.TextField(verbose_name='카카오아이디')),
                ('registerd_at', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
            ],
        ),
    ]
