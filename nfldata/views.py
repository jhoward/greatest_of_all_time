from django.shortcuts import render
from django.http import HttpResponse
from .models import Quarterback
from django.template import loader

# Create your views here.
def index(request):
    players = Quarterback.objects.all()
    #output = ' \n'.join([str(q) for q in Quarterback.objects.all()])
    template = loader.get_template('nfldata/base.html')
    context = {'players': players}
    return HttpResponse(template.render(context, request))
