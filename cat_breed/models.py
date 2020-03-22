#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel
from DjangoUeditor.models import UEditorField
SEX_CHOICES = [(x, x) for x in ['boy', 'girl', 'secret']]


class CatParentImg(BaseModel):
    img = models.ImageField(upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        pass



class CatParent(BaseModel):
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70, default='')
    sex = models.CharField(max_length=16, choices=SEX_CHOICES, default='secret')
    excerpt = UEditorField(width=800, height=500,
                           toolbars="full", imagePath="upimg/", filePath="upfile/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, blank=True
                           )
    img = models.ImageField(upload_to='cat_parent/%Y/%m/%d/', blank=True, null=True)
    imgs = models.ManyToManyField(CatParentImg, blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
       pass

    def __str__(self):
        return self.name


