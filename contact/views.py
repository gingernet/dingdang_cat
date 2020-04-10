#encoding=utf-8

import logging
from django.shortcuts import render
from contact.models import Contact


def contact(request):
    focus_point = "contact"
    contract_list = Contact.objects.all().order_by('-id')[:1]
    contract = contract_list[0]
    return render(request, 'contact/contact.html',locals())