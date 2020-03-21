#encoding=utf-8

import logging
from django.shortcuts import render

def contact(request):
    focus_point = "contact"
    return render(request, 'contact/contact.html',locals())