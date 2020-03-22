#encoding=utf-8

import logging
from django.shortcuts import render
from cat_breed.models import (
    CatParent,
    CatParentImg)
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger)
from django.core import serializers
from common.helper import ok_json, error_json


def cat_parents(request):
    focus_point = "cat_parents"
    page = request.GET.get('page')
    logging.info("page = %s", page)
    cat_parent_list = CatParent.objects.all()
    cat_parent_list = cat_parent_list.order_by("-created_at")
    paginator = Paginator(cat_parent_list, 50)
    try:
        cat_parent_list = paginator.page(page)
    except PageNotAnInteger:
        cat_parent_list = paginator.page(1)
    except EmptyPage:
        cat_parent_list = paginator.page(paginator.num_pages)
    if request.is_ajax():
        json_data = serializers.serialize("json", cat_parent_list, ensure_ascii=False)
        return ok_json({'cat_parent_list': json_data})
    return render(request, 'cat_breed/cat_parents.html',locals())


def cat_parents_detail(request, cid):
    img_ids = []
    focus_point = "cat_parents"
    cat_parent = CatParent.objects.get(id=cid)
    for cat_img in cat_parent.imgs.all():
        img_ids.append(cat_img.id)
    if request.is_ajax():
        json_data = serializers.serialize("json", cat_parent, ensure_ascii=False)
        return ok_json({'cat_parent': json_data})
    return render(request, 'cat_breed/cat_parents_detail.html', locals())


def cat_certificate(request):
    focus_point = "cat_certificate"
    return render(request, 'cat_breed/cat_certificate.html', locals())



