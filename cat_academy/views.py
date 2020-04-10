#encoding=utf-8

import logging
from django.shortcuts import render


def find_normal_house(request):
    focus_point = "find_normal_house"
    return render(request, 'cat_academy/find_normal_house.html',locals())


def diet_manger(request):
    focus_point = "diet_manger"
    return render(request, 'cat_academy/diet_manger.html', locals())


def behave_living(request):
    focus_point = "behave_living"
    return render(request, 'cat_academy/behave_living.html', locals())


def health_disease(request):
    focus_point = "health_disease"
    return render(request, 'cat_academy/health_disease.html', locals())


def others(request):
    focus_point = "others"
    return render(request, 'cat_academy/behave_living.html', locals())


def find_normal_house_detail(request):
    focus_point = "find_normal_house"
    return render(request, 'cat_academy/find_normal_house_detail.html',locals())

