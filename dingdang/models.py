#encoding=utf-8

from django.db import models


class BaseModelManager(models.Manager):
    def all_to_dict(self):
        queryset = self.get_queryset()
        return [obj.to_dict() for obj in queryset.all()]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.id)


class Banner(BaseModel):
    text_info = models.CharField('图片描述', max_length=50, default='')
    img = models.ImageField('图片', upload_to='banner/')
    link_url = models.URLField('图片URL', max_length=100)
    is_active = models.BooleanField('是否显示该图片', default=False)

    class Meta:
        verbose_name = '首页banner'
        verbose_name_plural = '首页banner'

    def __str__(self):
        return self.text_info







