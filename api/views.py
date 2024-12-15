import random
from django.http import JsonResponse
from firebase_admin import firestore
import json

db = firestore.client()

def question(request):
    if (request.method == 'POST'):

        ## message firestore
        message_ref = db.collection(u'messages').document()

        data = json.loads(request.body)

        message = data.get("message", "No message provided")

        USER_ID = "1"

        ## insert document

        
        print(f"User {USER_ID} asked: {message}")
        # Listas de contenidos posibles
        css_options = [
            "body { background-color: lightblue; } #content { color: darkblue; font-size: 20px; text-align: center; }",
            "body { background-color: lightgreen; } #content { color: darkgreen; font-size: 18px; text-align: left; }",
            "body { background-color: lightcoral; } #content { color: darkred; font-size: 22px; text-align: right; }",
            "body { background-color: lightyellow; } #content { color: darkorange; font-size: 24px; text-align: center; }",
            "body { background-color: lavender; } #content { color: darkviolet; font-size: 20px; text-align: justify; }",
            "body { background-color: pink; } #content { color: purple; font-size: 18px; text-align: left; font-family: Arial, sans-serif; }",
            "body { background-color: beige; } #content { color: #5A5A5A; font-size: 20px; text-align: center; font-style: italic; }",
            "body { background-color: lightgray; } #content { color: black; font-size: 16px; text-align: right; font-weight: bold; }",
        ]
        
        html_options = [    
            "<h1>Bienvenido a nuestro sitio</h1><p>El contenido cambia con cada carga.</p>",
            "<h1>¡Saludos desde Django!</h1><p>Este es un ejemplo de contenido dinámico.</p>",
            "<h1>Bienvenido al iframe dinámico</h1><p>El contenido se genera aleatoriamente.</p>",
            "<h1>Contenido dinámico generado</h1><p>Cada vez que se recarga, el contenido cambia.</p>",
            "<h1>¡Nuevo contenido cada vez!</h1><p>Este es un ejemplo de contenido que cambia constantemente.</p>",
            "<h1>Contenido variable</h1><p>Cada vez que visitas, ves algo diferente.</p>",
            "<h1>¡Cambio de contenido en acción!</h1><p>Este contenido es generado de forma aleatoria y única.</p>",
        ]
        
        js_options = [
            "console.log('Contenido JS vacío');"
        ]
        
        # Seleccionar un contenido aleatorio de cada lista
        css = random.choice(css_options)
        html = random.choice(html_options)
        js = random.choice(js_options)
        
        # Crear el diccionario con los contenidos aleatorios
        data = {
            "css": css,
            "html": html,
            "js": js,
        }

        ## insert document
        message_ref.set({
            u'user_id': USER_ID,
            u'message': message,
            u'response': data,
            u'created_at': firestore.SERVER_TIMESTAMP
        })
        
        return JsonResponse(data)

def historial_messages(request):
    if request.method == 'GET':
        USER_ID = "1"  # ID del usuario que deseas filtrar

        # Traer todos los mensajes con el `user_id` especificado
        messages_ref = db.collection(u'messages').where(u'user_id', u'==', USER_ID).stream()

        # Convertir documentos en una lista de diccionarios
        messages_list = [message.to_dict() for message in messages_ref]

        # Ordenar los mensajes por `created_at` en orden descendente
        sorted_messages = sorted(
            messages_list,
            key=lambda x: x['created_at'],  # Asegúrate de que `created_at` exista en cada documento
            reverse=True
        )

        # Obtener solo los últimos 3 mensajes
        data = sorted_messages[:10]

        # Retornar los datos en formato JSON
        return JsonResponse(data, safe=False)