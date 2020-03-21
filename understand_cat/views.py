#encoding=utf-8

import logging
from django.shortcuts import render


def color_suit(request):
    focus_point = "color_suit"
    return render(request, 'understand_cat/color_suit.html',locals())


def cat_profile(request):
    focus_point = "cat_profile"
    return render(request, 'understand_cat/cat_profile.html', locals())


def breed_history(request):
    focus_point = "breed_history"
    return render(request, 'understand_cat/breed_history.html', locals())


def phase_identification(request):
    focus_point = "phase_identification"
    return render(request, 'understand_cat/phase_identification.html', locals())



