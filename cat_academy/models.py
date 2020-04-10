#encoding=utf-8

from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from dingdang.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    index = models.IntegerField(default=999)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Tui(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = models.CharField(max_length=70)
    excerpt = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', blank=True, null=True)
    body = UEditorField(width=800, height=500,
                            toolbars="full", imagePath="upimg/", filePath="upfile/",
                            upload_settings={"imageMaxSize": 1204000},
                            settings={}, command=None, blank=True
                        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
       pass

    def __str__(self):
        return self.title


