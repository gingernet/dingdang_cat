from django.contrib import admin
from buy_cat.models import CatBuy, CatBuyImg, BuyCatInfo


@admin.register(CatBuyImg)
class CatBuyImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')


@admin.register(CatBuy)
class CatBuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'sex', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


@admin.register(BuyCatInfo)
class BuyCatInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'weichat', 'city', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'name')


