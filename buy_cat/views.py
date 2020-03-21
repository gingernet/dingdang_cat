#encoding=utf-8

import logging
from django.shortcuts import render


def for_sale(request):
    focus_point = "for_sale"
    return render(request, 'buy_cat/for_sale.html',locals())


def breed_plan(request):
    focus_point = "breed_plan"
    return render(request, 'buy_cat/breed_plan.html', locals())


def price_range(request):
    focus_point = "price_range"
    return render(request, 'buy_cat/price_range.html', locals())


def pedigree_and_health(request):
    focus_point = "pedigree_and_health"
    return render(request, 'buy_cat/pedigree_and_health.html', locals())


def purchase_process(request):
    focus_point = "purchase_process"
    return render(request, 'buy_cat/purchase_process.html', locals())


def for_sale_detail(request):
    focus_point = "for_sale"
    return render(request, 'buy_cat/for_sale_detail.html', locals())
