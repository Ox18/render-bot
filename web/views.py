from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def chat(request):
    template = loader.get_template('chat.html')
    return HttpResponse(template.render())

def receptor(request):
    template = loader.get_template('receptor.html')
    return HttpResponse(template.render())