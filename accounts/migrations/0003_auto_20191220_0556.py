# Generated by Django 3.0 on 2019-12-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191219_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='token',
            options={'verbose_name': '토큰', 'verbose_name_plural': '토큰'},
        ),
        migrations.RemoveField(
            model_name='token',
            name='device_token',
        ),
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.CharField(max_length=55, verbose_name='엑세스토큰'),
        ),
    ]
