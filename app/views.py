from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import os
# Create your views here.


def index(request):
    template = loader.get_template("../templates/index.html")
    return HttpResponse(template.render())


def clicked_button(request):
    os.system("shutdown /s /t 1")
    return HttpResponse("Komputer został wyłączony XD")
