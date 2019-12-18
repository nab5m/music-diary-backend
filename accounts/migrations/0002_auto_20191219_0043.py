# Generated by Django 3.0 on 2019-12-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(max_length=55, verbose_name='디바이스토큰')),
                ('access_token', models.CharField(blank=True, max_length=55, null=True, verbose_name='엑세스토큰')),
                ('expires_in', models.DateTimeField(blank=True, null=True, verbose_name='엑세스토큰_만료시간')),
                ('refresh_token', models.CharField(blank=True, max_length=55, null=True, verbose_name='연장토큰')),
                ('refresh_token_expires_in', models.DateTimeField(blank=True, null=True, verbose_name='연장토큰_만료시간')),
                ('scope', models.CharField(blank=True, max_length=55, null=True, verbose_name='조회범위')),
            ],
            options={
                'verbose_name': '카카오계정',
                'verbose_name_plural': '카카오계정',
            },
        ),
        migrations.AlterModelOptions(
            name='kakaoaccounts',
            options={'verbose_name': '카카오계정', 'verbose_name_plural': '카카오계정'},
        ),
        migrations.AddField(
            model_name='kakaoaccounts',
            name='age_range',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='연령대'),
        ),
        migrations.AddField(
            model_name='kakaoaccounts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='카카오계정이메일'),
        ),
        migrations.AddField(
            model_name='kakaoaccounts',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='kakaoaccounts',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='닉네임'),
        ),
        migrations.AddField(
            model_name='kakaoaccounts',
            name='thumbnail_image',
            field=models.URLField(blank=True, null=True, verbose_name='프사_URL'),
        ),
        migrations.AlterField(
            model_name='kakaoaccounts',
            name='kakao_id',
            field=models.TextField(unique=True, verbose_name='카카오아이디'),
        ),
    ]
