import random
from django.http import JsonResponse

def main(request):
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
        "console.log('Contenido JS vacío');",
        "console.log('Este es un mensaje de JavaScript');",
        "alert('¡Este es un mensaje de alerta en JS!');",
        "console.log('Generando contenido dinámico con JS');",
        "alert('Contenido JavaScript: alert');",
        "console.log('Cargando nuevas funcionalidades...');",
        "document.body.style.backgroundColor = 'lightblue';",
        "document.getElementById('content').innerHTML = '<p>Nuevo contenido cargado con JS</p>';",
        "alert('¡El contenido se ha actualizado dinámicamente con JS!');",
        "console.log('Recargando contenido dinámico mediante JS');",
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
    
    return JsonResponse(data)
