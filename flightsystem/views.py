from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import requests as req
import json

from .models import City


def index(request):
    # city_list = City.objects.all()
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

# @require_http_methods(["GET"])
# def init_city(request):
#     response = {}
#     try:
#         # City.objects.create()
#         city_list = get_city_list()
#         for city in city_list:
#             City.objects.create(city_code=city['code'], city_name=city['name'])
#         response['msg'] = 'success'
#         response['error_num'] = 0
#         response['data'] = city_list
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1
#     return JsonResponse(response)
#
#
# def get_airport():
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
#     res = req.get('https://flights.ctrip.com/schedule/poi/get', headers=headers)
#     return json.loads(res.text)
#
#
# def get_city_list():
#     res = get_airport()
#     airport_list = []
#     airport_key = list(res['data'].keys())
#     if '热门' in airport_key:
#         airport_key.remove('热门')
#     for item in airport_key:
#         keys = list(res['data'][item].keys())
#         for key in keys:
#             value = res['data'][item][key]
#             for airport in value:
#                 element = {
#                     'name': airport['display'].split('(')[0],
#                     'code': airport['data'].split('|')[3].split(',')[0]
#                 }
#                 if element not in airport_list:
#                     airport_list.append(element)
#     return airport_list
