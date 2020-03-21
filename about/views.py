#encoding=utf-8

import logging
from django.shortcuts import render


def about_house(request):
    focus_point = "about_house"
    return render(request, 'about/about_house.html',locals())

def about_idea(request):
    focus_point = "about_idea"
    return render(request, 'about/about_idea.html', locals())


