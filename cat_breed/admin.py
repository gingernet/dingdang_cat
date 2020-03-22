from django.contrib import admin
from cat_breed.models import CatParentImg, CatParent


@admin.register(CatParentImg)
class CatParentImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')


@admin.register(CatParent)
class CatParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'excerpt', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')
