# Generated by Django 3.0 on 2020-02-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='노래 번호')),
                ('title', models.CharField(max_length=255, verbose_name='노래 제목')),
                ('thumbnail_image_url', models.URLField(verbose_name='썸네일 이미지 주소')),
                ('artist', models.CharField(max_length=255, verbose_name='가수')),
            ],
            options={
                'verbose_name': '노래',
                'verbose_name_plural': '노래',
            },
        ),
    ]