#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel
from DjangoUeditor.models import UEditorField
SEX_CHOICES = [(x, x) for x in ['boy', 'girl', 'secret']]


class CatBuyImg(BaseModel):
    img = models.ImageField("图片", upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        verbose_name = "小猫图片"
        verbose_name_plural = "小猫图片"


class CatBuy(BaseModel):
    name = models.CharField("名字", max_length=70)
    color = models.CharField("颜色", max_length=70, default='')
    sex = models.CharField("性别", max_length=16, choices=SEX_CHOICES, default='secret')
    excerpt = UEditorField("简介", width=800, height=500,
                           toolbars="full", imagePath="upimg/", filePath="upfile/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, blank=True
                           )
    img = models.ImageField("封面", upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)
    imgs = models.ManyToManyField(CatBuyImg, blank=True)
    views = models.PositiveIntegerField("浏览次数", default=0)

    class Meta:
        verbose_name = "待售小猫"
        verbose_name_plural = "待售小猫"

    def __str__(self):
        return self.name


class BuyCatInfo(BaseModel):
    BUY_CHOICES = [(x, x) for x in ['YES', 'NO']]
    name = models.CharField("名字", max_length=70)
    phone = models.CharField("电话", max_length=16)
    weichat = models.CharField("微信", max_length=16)
    position = models.CharField("职业", max_length=16)
    city = models.CharField("城市", max_length=16)
    is_breed = models.CharField(max_length=100, choices=BUY_CHOICES)
    is_guo = models.CharField(max_length=100, choices=BUY_CHOICES)
    is_love = models.CharField(max_length=100, choices=BUY_CHOICES)

    class Meta:
        verbose_name = "用户购买猫信息"
        verbose_name_plural = "用户购买猫信息"

    def __str__(self):
        return self.name




