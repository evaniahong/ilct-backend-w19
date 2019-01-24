from django.http import HttpResponse
from django.template import loader

from .models import Business

from django.shortcuts import get_object_or_404, render


def index(request):
    business_list = Business.objects.all()
    template = loader.get_template('business/index.html')
    context = {
        'business_list': business_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, business_id):
    business_list = Business.objects.all()
    template = loader.get_template('business/detail.html')
    context = {
        'business':  Business.objects.get(pk= business_id),
    }
    return HttpResponse(template.render(context, request))