import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from journal_manage_system import models


@require_http_methods(['GET'])
def add_catalogs(request):
    response = {}
    try:
        new_item = models.Catalog(journal_name=request.GET.get('journal_name'))
        new_item.publisher = {'publisher': '测试出版社'}
        new_item.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(['GET'])
def show_catalogs(request):
    response = {}
    try:
        new_item = models.Catalog.objects.all()
        response['list'] = json.loads(serializers.serialize("json", new_item))
        response['msg'] = "success"
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
