#encoding=utf-8

from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from dingdang.models import BaseModel


class Category(BaseModel):
    name = models.CharField("名称",max_length=100)
    index = models.IntegerField(default=999)

    class Meta:
        verbose_name = "养猫学院类别"
        verbose_name_plural = "养猫学院类别"

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = models.CharField("标题", max_length=70)
    excerpt = models.TextField("摘要", max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    img = models.ImageField("封面图片", upload_to='article_img/%Y/%m/%d/', blank=True, null=True)
    body = UEditorField("文章内容", width=800, height=500,
                        settings={}, command=None, blank=True
                        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField("查看次数", default=0)

    class Meta:
        verbose_name = "养猫文章"
        verbose_name_plural = "养猫文章"

    def __str__(self):
        return self.title


