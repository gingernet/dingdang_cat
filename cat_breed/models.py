#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel
from DjangoUeditor.models import UEditorField
SEX_CHOICES = [(x, x) for x in ['boy', 'girl', 'secret']]


class CatParentImg(BaseModel):
    img = models.ImageField("图片", upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = "图片表"
        verbose_name_plural = "图片表"



class CatParent(BaseModel):
    name = models.CharField("名字", max_length=70)
    color = models.CharField("颜色", max_length=70, default='')
    sex = models.CharField("性别", max_length=16, choices=SEX_CHOICES, default='secret')
    excerpt = UEditorField("简介", width=800, height=500,
                           toolbars="full", imagePath="upimg/", filePath="upfile/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, blank=True
                           )
    img = models.ImageField("封面", upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)
    imgs = models.ManyToManyField(CatParentImg, blank=True)
    views = models.PositiveIntegerField("浏览次数", default=0)

    class Meta:
        verbose_name = "猫妈猫爸"
        verbose_name_plural = "猫妈猫爸"

    def __str__(self):
        return self.name


