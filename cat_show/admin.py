from django.contrib import admin
from cat_show.models import ShowCategory, ShowImg


@admin.register(ShowCategory)
class ShowCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(ShowImg)
class ShowImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'user', 'views', 'created_at')
    list_per_page = 50
    ordering = ('-created_at',)
    list_display_links = ('id', 'title')


