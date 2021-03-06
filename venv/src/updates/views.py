from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize

from .models import Update
from cfiapi.mixins import JsonResponseMixin
import json


def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "context": "Some new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.get(id=1).serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
