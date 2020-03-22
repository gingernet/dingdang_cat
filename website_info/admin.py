#encoding=utf-8

from django.contrib import admin
from website_info.models import Link

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'linkurl')
