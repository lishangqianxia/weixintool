# coding:utf-8

from django.http import HttpResponse, JsonResponse, FileResponse
from thirdparty import juhe
from django.views import View
from utils.response import CommonResponseMixin
import json


class SimpleWeather(View, CommonResponseMixin):
    def get(self, request):
        pass

    def post(self, request):
        if request.method == 'GET':
            city = request.GET.get('city')
            data = []
            result = juhe.simpleWeather(city)
            data.append(result)
            return JsonResponse(data=data, safe=False)

        elif request.method == 'POST':
            data = []
            received_body = request.body.decode('utf-8')
            received_body = json.loads(received_body)
            cities = received_body.get('cities')
            for city in cities:
                # city = city.get('city')
                result = juhe.simpleWeather(city)
                data.append(result)
            response_data = self.wrap_json_response(data)
            print(response_data)
            return JsonResponse(data=data, safe=False)


