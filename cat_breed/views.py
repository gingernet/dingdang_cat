#encoding=utf-8

import logging
from django.shortcuts import render


def cat_parents(request):
    focus_point = "cat_parents"
    return render(request, 'cat_breed/cat_parents.html',locals())


def cat_certificate(request):
    focus_point = "cat_certificate"
    return render(request, 'cat_breed/cat_certificate.html', locals())


def cat_parents_detail(request):
    return render(request, 'cat_breed/cat_parents_detail.html', locals())
