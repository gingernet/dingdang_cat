#encoding=utf-8

import logging
from django.shortcuts import render


def website_map(request):
    focus_point = "website_map"
    return render(request, 'website_info/website_map.html',locals())


def legal_notices(request):
    focus_point = "legal_notices"
    return render(request, 'website_info/legal_notices.html', locals())


def friends_link(request):
    focus_point = "friends_link"
    return render(request, 'website_info/friends_link.html', locals())



