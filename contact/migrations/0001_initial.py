# Generated by Django 2.2.3 on 2020-03-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('num_public', models.CharField(default='', max_length=70)),
                ('num_weichat', models.CharField(default='', max_length=70)),
                ('sina_weibo', models.CharField(default='', max_length=70)),
                ('num_qq', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('manager', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
