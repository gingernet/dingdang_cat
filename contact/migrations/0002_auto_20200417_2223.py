# Generated by Django 2.2.3 on 2020-04-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': '网站联系信息表', 'verbose_name_plural': '网站联系信息表'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=70, verbose_name='电子邮件'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='manager',
            field=models.CharField(default='', max_length=70, verbose_name='管理员名字'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_public',
            field=models.CharField(default='', max_length=70, verbose_name='公众号'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_qq',
            field=models.CharField(default='', max_length=70, verbose_name='QQ号'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_weichat',
            field=models.CharField(default='', max_length=70, verbose_name='微信号'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sina_weibo',
            field=models.CharField(default='', max_length=70, verbose_name='新浪微博'),
        ),
    ]
