# Generated by Django 2.2.3 on 2020-03-21 23:40

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatParentImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='cat_parent/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='CatParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=70)),
                ('excerpt', DjangoUeditor.models.UEditorField(blank=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('imgs', models.ManyToManyField(blank=True, to='cat_breed.CatParentImg')),
            ],
        ),
    ]
