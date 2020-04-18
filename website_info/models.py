#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel


class Link(BaseModel):
    name = models.CharField("名字", max_length=20)
    img = models.ImageField("图片", upload_to='link/')
    linkurl = models.URLField("URL", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'