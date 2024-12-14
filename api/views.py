from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def api(request):
    return HttpResponse("Hello, World!")

def question(request):
    data = {
        "css": "body { background-color: lightblue; } #content { color: darkblue; font-size: 20px; text-align: center; }",
        "html": "<h1>¡Hola desde el iframe!</h1><p>Este contenido fue renderizado dinámicamente.</p>",
        "js": "",
    }
    return JsonResponse(data)