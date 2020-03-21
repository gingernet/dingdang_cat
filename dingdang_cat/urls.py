#encoding=utf-8

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from dingdang.views import index
from about.views import about_idea, about_house
from contact.views import contact
from cat_breed.views import (
    cat_certificate,
    cat_parents,
    cat_parents_detail)

from buy_cat.views import (
    for_sale,
    breed_plan,
    price_range,
    pedigree_and_health,
    purchase_process,
    for_sale_detail)

from understand_cat.views import (
    color_suit,
    cat_profile,
    breed_history,
    phase_identification)

from cat_show.views import history_pictures, cat_new_home

from cat_academy.views import (
    find_normal_house,
    diet_manger,
    behave_living,
    health_disease,
    others,
    find_normal_house_detail)

from website_info.views import (
    website_map,
    legal_notices,
    friends_link)

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'', index, name='index'),

    path(r'about_house', about_house, name='about_house'),
    path(r'about_idea', about_idea, name='about_idea'),

    path(r'cat_certificate', cat_certificate, name='cat_certificate'),
    path(r'cat_parents', cat_parents, name='cat_parents'),
    path(r'cat_parents_detail', cat_parents_detail, name='cat_parents_detail'),

    path(r'for_sale', for_sale, name='for_sale'),
    path(r'for_sale_detail', for_sale_detail, name='for_sale_detail'),
    path(r'breed_plan', breed_plan, name='breed_plan'),
    path(r'price_range', price_range, name='price_range'),
    path(r'pedigree_and_health', pedigree_and_health, name='pedigree_and_health'),
    path(r'purchase_process', purchase_process, name='purchase_process'),

    path(r'color_suit', color_suit, name='color_suit'),
    path(r'cat_profile', cat_profile, name='cat_profile'),
    path(r'breed_history', breed_history, name='breed_history'),
    path(r'phase_identification', phase_identification, name='phase_identification'),

    path(r'history_pictures', history_pictures, name='history_pictures'),
    path(r'cat_new_home', cat_new_home, name='cat_new_home'),

    path(r'find_normal_house', find_normal_house, name='find_normal_house'),
    path(r'diet_manger', diet_manger, name='diet_manger'),
    path(r'behave_living', behave_living, name='behave_living'),
    path(r'health_disease', health_disease, name='health_disease'),
    path(r'others', others, name='others'),
    path(r'find_normal_house_detail', find_normal_house_detail, name='find_normal_house_detail'),

    path(r'website_map', website_map, name='website_map'),
    path(r'legal_notices', legal_notices, name='legal_notices'),
    path(r'friends_link', friends_link, name='friends_link'),

    path(r'contact', contact, name='contact')
]
