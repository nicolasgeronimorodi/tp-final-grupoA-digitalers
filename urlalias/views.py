from django import views
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .forms import URLForm2
from .models import URLAlias, TestURLAlias
import nanoid

import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


_NANO_DICT = "abcdefz-"

@method_decorator(csrf_exempt, name='dispatch')
class Api(views.View):
    model=TestURLAlias
    def post(self, request):
        data=json.loads(request.body.decode("utf-8")   )
        print(f" data es {data} y es de tipo {type(data)}"   )
        url=data.get('url')
        print(f"url es {url} y es de tipo {type(url)}")
        
        
        Url=TestURLAlias(fullurl=url)
        alias=nanoid.generate(alphabet=_NANO_DICT, size=5)
        Url.alias=alias
        Url.save()

        response={"alias": alias}
        print(f"response es {response}")
        return JsonResponse(response, status=201)
    def get(self, request):
        return JsonResponse({"mensaje": "funciona"})
