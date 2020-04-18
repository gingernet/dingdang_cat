#encoding=utf-8

from django.db import models
from django.contrib.auth.models import User
from dingdang.models import BaseModel


class ShowCategory(BaseModel):
    name = models.CharField("名称",max_length=100)
    index = models.IntegerField(default=999)

    class Meta:
        verbose_name = "图片展览类别"
        verbose_name_plural = "图片展览类别"

    def __str__(self):
        return self.name


class ShowImg(BaseModel):
    title = models.CharField("标题", max_length=70)
    category = models.ForeignKey(ShowCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    img = models.ImageField("封面图片", upload_to='show_img/%Y/%m/%d/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField("查看次数", default=0)

    class Meta:
        verbose_name = "图片展览"
        verbose_name_plural = "图片展览"

    def __str__(self):
        return self.title


