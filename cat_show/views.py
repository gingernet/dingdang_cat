#encoding=utf-8

import logging
from django.shortcuts import render


def history_pictures(request):
    focus_point = "history_pictures"
    return render(request, 'cat_show/history_pictures.html',locals())

def cat_new_home(request):
    focus_point = "cat_new_home"
    return render(request, 'cat_show/cat_new_home.html', locals())
