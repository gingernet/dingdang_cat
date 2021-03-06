# Generated by Django 2.2.3 on 2020-04-18 04:27

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '养猫文章', 'verbose_name_plural': '养猫文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '养猫学院类别', 'verbose_name_plural': '养猫学院类别'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tui',
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='article_img/%Y/%m/%d/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=70, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='查看次数'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名称'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='Tui',
        ),
    ]
