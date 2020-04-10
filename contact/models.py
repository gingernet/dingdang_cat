#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel


class Contact(BaseModel):
    num_public = models.CharField('公众号', max_length=70, default='')
    num_weichat = models.CharField('微信号', max_length=70, default='')
    sina_weibo = models.CharField('新浪微博', max_length=70, default='')
    num_qq = models.CharField('QQ号', max_length=70, default='')
    email = models.CharField('电子邮件', max_length=70, default='')
    phone = models.CharField('手机号码', max_length=70, default='')
    manager = models.CharField('管理员名字', max_length=70, default='')

    class Meta:
        verbose_name = '网站联系信息表'
        verbose_name_plural = '网站联系信息表'

    def __str__(self):
        return self.num_public

