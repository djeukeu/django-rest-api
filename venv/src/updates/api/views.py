from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse


class UpdateModelAPIView(View):
    '''
    Retrieve, Update, Delete ---> Object
    '''

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return

    def put(self, request, *args, **kwargs):
        return

    def delete(self, request, *args, **kwargs):
        return


class UpdateModelListAPIView(View):
    '''
    List View
    Create View
    '''

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')
