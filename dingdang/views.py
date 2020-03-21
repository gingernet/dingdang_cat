#encoding=utf-8

import logging
from django.shortcuts import render


def index(request):
    focus_point = "index"
    return render(request, 'index/index.html',locals())


