#encoding=utf-8

from django.db import models
from dingdang.models import BaseModel

class Link(BaseModel):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='link/')
    linkurl = models.URLField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        pass