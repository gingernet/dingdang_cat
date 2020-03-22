#encoding=utf-8

from django.contrib import admin
from dingdang.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

