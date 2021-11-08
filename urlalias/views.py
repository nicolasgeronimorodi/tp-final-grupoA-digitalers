from os import read
from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .forms import URLForm2
from .models import URLAlias, TestURLAlias, Visitas_ind
import nanoid

import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#from requests import get#validar url
from ipware import get_client_ip

# Create your views here.

# importar variables externas del archivo VariablesExternas.txt
#===============================================================
from io import open
import re

texto=open("VariablesExternas.txt","r", encoding="utf-8")
variables=texto.readlines()
texto.close()
host_dir=(re.sub(r'.', '', variables[0], count = 9)).rstrip()
#variable_2=(re.sub(r'.', '', variables[1], count = 11)).rstrip()
#===============================================================



"""
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
        return JsonResponse({"mensaje": "funciona"})"""

imagen_1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠒⠈⠉⠉⠉⠉⠒⠀⠀⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⠀⠑⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠿⠿⠣⣶⣿⡏⣶⣿⣿⠷⠶⠆⠀⠀⠘⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠴⡅⠀⠀⠠⢶⣿⣿⣷⡄⣀⡀⡀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⣰⡶⣦⠀⠀⠀⡰⠀⠀⠸⠟⢸⣿⣿⣷⡆⠢⣉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣧⣿⣇⠀⠀⡇⠀⢠⣷⣲⣺⣿⣿⣇⠤⣤⣿⣿⠀⢸⠀⣤⣶⠦⠀⠀⠀⠀
⠀⠀⠙⢿⣿⣦⡀⢇⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⡜⣾⣿⡃⠇⢀⣤⡀⠀
⠀⠀⠀⠀⠙⢿⣿⣮⡆⠀⠙⠿⣿⣿⣾⣿⡿⡿⠋⢀⠞⢀⣿⣿⣿⣿⣿⡟⠁⠀
⠀⠀⠀⠀⠀⠀⠛⢿⠇⣶⣤⣄⢀⣰⣷⣶⣿⠁⡰⢃⣴⣿⡿⢋⠏⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢾⣿⣿⣿⣞⠿⣿⣿⢿⢸⣷⣌⠛⠋⠀⠘⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠙⣿⣿⣿⣶⣶⣿⣯⣿⣿⣿⣆⠀⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣯⡙⢿⣿⣿⠟⡁⠰⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⡟⠈⢩⣥⣾⣷⠐⡌⠙⠃⠀"""

imagen_2 ="""
⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇
⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽
⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣"""

imagen_3 = """
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⠿⣫⣥⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⠾⢿⢟⣵⣾⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣰⡿⣀⣤⣴⣾⣿⡇⠙⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣴⣿⣿⠿⠛⠉⢩⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⡀⠄⠄⠄⠄
⠄⠄⠄⠄⠈⠛⠉⠄⠄⠄⠄⢸⣿⣿⡇⠄⠄⠄⠄⠄⠄⢀⣼⡿⣫⣾⠆⠄⠄⠄
⠄⠄⠄⠄⢀⣶⣶⣶⣶⣶⣶⣿⣿⣿⠇⠄⠄⠄⣠⣎⣠⣴⣶⠎⠛⠁⠄⠄⠄⠄
⠄⠄⠄⠄⣾⣿⣿⣿⣿⠿⠿⠟⠛⠋⠄⠄⢀⣼⣿⠿⠛⣿⡟⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠛⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠉⠄⠄⢸⣿⡇⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⣿⣿⣿⡿⠿⠃⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄"""

imagen_4 = """
⠻⣦⡈⠛⢿⡌⢆⢂⠹⣿⣧⡄⡄⠹⡄⢆⡟⢄⠉⢟⣮⣷⢄⠐⢤⡤⢤⣬⣭⣭
⣷⣤⠙⣶⣦⠙⡌⢻⠂⠘⣿⣷⢹⠄⢳⠘⣿⡟⣿⡄⢳⡆⢳⠛⢢⠈⠉⠛⠛⠛
⢿⣿⣷⣀⠈⠓⠌⠂⠘⢆⠈⢙⣎⢣⠘⡆⢣⡛⣿⡇⢀⡙⠚⠶⠶⠿⠷⠶⠒⠒
⣾⠿⣿⣿⣦⣄⣁⣀⣠⡀⠡⠄⠳⡛⢆⠱⠈⢧⣿⡇⠸⠟⠉⠐⠠⠄⠄⠄⣼⣿
⣿⣷⣬⣉⣛⣛⠛⠿⠿⣧⣷⣦⣄⠘⢿⡆⠡⠘⣀⡇⢠⣶⣷⣮⣤⣤⣴⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢿⡀⠄⠉⡇⢸⣿⣿⣿⣉⣉⣉⣉⣉⣰
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣦⡙⠄⠄⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⣿⣿⣷⣌⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣦⣀⡨⣝⡻⠿⣻⣿⣧⣄⠄⠄⣿⣿⣿⣿⣿⣦⡀⢻⣿⣿⣿⣿⣿⡿⠿⣿
⣿⣿⣿⣿⡇⢿⡛⢿⣿⣿⣿⣿⣧⠘⣿⣛⣻⣿⣿⣿⣿⣤⡿⢿⠿⣛⡃⠄⣸⣿
⡹⣿⣿⣿⣿⣼⣷⣶⣝⢿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⢇⣈⣼⣿⣿
⣿⣜⢿⣭⢻⣿⣿⣿⣯⢧⠙⢻⠛⣛⣛⠛⠛⠿⠿⠟⣛⣥⣶⣼⢏⣾⣿⣿⣿⣿
⣿⣿⣎⠿⣇⢻⣿⣿⣿⡌⢷⣆⢭⣓⣒⣒⣛⣣⣶⠞⣵⣿⣿⣿⡿⣱⣾⡟⣵⣿
⣿⣿⣿⣤⣻⡘⣿⣿⣿⣷⡜⢻⣮⣛⣛⣟⣫⡿⣛⣴⣿⣿⣿⣿⢃⣿⣿⣷⣿⣿
⣿⣿⣿⣿⣷⣣⢹⣿⣿⣿⣿⣯⡙⠛⠛⠛⢛⣺⣿⣿⣿⣿⣿⠇⣼⢫⣵⣿⣿⣿"""


@method_decorator(csrf_exempt, name='dispatch')
class Api(views.View):
    model=TestURLAlias
    def post(self, request):
        data=json.loads(request.body.decode("utf-8")   )
        print(f" data es {data} y es de tipo {type(data)}"   )
        url=data.get('url')
        print(f"url es {url} y es de tipo {type(url)}")

        """
        try: #prueba conectarse a una pagina quiza sirva para la validacion aunque si la pagina está temporalmente caida seria un falso negativo
            get(url, timeout = 3)
            print("VALIDO")
        except:
            print("NO VALIDO")
            print(imagen_5)
        """

        try:#evito guardar varias veces el mismo link
            link = url
            obj = TestURLAlias.objects.get(fullurl=link)
            alias_parcial = (obj.alias)
            print(imagen_1)
            print("          LINK REPETIDO")
            #print(f"alias asignado: {obj.alias}")
        except:

            Url=TestURLAlias(fullurl=url)
            alias_r = nanoid.generate(size=7)#nanoid
            #alias_r = "dZKrFN7"#prueba de de alias repetido
            
            while True:#con esto pretendo evitar que se guarden alias iguales
               
                try: 
                    alias_enc = TestURLAlias.objects.get(alias = alias_r)
                    alias_r = nanoid.generate(size=7)#nanoid
                    print(imagen_3)
                    print(f"          ALIAS REPETIDO: {alias_enc.alias}")
                except:
                    alias_parcial = alias_r
                    break

            Url.alias=alias_parcial
            Url.save()
            print(imagen_2)
            print("          LINK NUEVO")
        #alias = f"http://127.0.0.1:8000/r/{alias_parcial}"
        alias = f"{host_dir}r/{alias_parcial}"

        response={"alias": alias}
        print(f"response es {response}")
        return JsonResponse(response, status=201)

def redir(request, pk):#redirecciona al enlace original
    
    try:#tiene una funcion de contar visitas basica

        te_encontre = TestURLAlias.objects.get(alias=pk)
        
#===============================================================
        ip_us, is_routable = get_client_ip(request)

        if ip_us is None:

            ip_us ="0.0.0.0"
        else:
            if is_routable:
                ipv="Public"
            else:
                ipv="Private"
#===============================================================

        try:

            obj_vis = Visitas_ind.objects.get(ip = ip_us, alias = pk)

            print("BIENVENIDO NUEVAMENTE")
            print(f"Usuario=> {obj_vis.ip}, Alias=> {obj_vis.alias}")

        except:
            
            Url_v=Visitas_ind(alias=pk)
            Url_v.ip=ip_us
            Url_v.save()
            print("NUEVA VISITA")
            contador = te_encontre.visitas
            te_encontre.visitas = contador + 1
            te_encontre.save()


        print(f"\nCantidad de visitas=> {te_encontre.visitas}")

        print(imagen_4)
        redireccionar = te_encontre.fullurl

    except:#en caso de no encontrar el link en la base de datos se podria poner otra pagina con un mensaje en plan "URL no encontrado"
        #de momento lo envio al home
        redireccionar = f"{host_dir}"
        #redireccionar = "http://127.0.0.1:8000/"

        print(imagen_3)
        print("          PANICO.jpg\n")

    return redirect(redireccionar)
