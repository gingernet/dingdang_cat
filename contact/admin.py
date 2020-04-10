from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_weichat', 'sina_weibo', 'num_qq', 'email', 'phone', 'manager')
