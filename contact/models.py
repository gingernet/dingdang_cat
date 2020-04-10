#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel


class Contact(BaseModel):
    num_public = models.CharField(max_length=70, default='')
    num_weichat = models.CharField(max_length=70, default='')
    sina_weibo = models.CharField(max_length=70, default='')
    num_qq = models.CharField(max_length=70, default='')
    email = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=70, default='')
    manager = models.CharField(max_length=70, default='')

    class Meta:
       pass

    def __str__(self):
        return self.num_public

