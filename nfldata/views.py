from django.shortcuts import render
from django.http import HttpResponse
from .models import Quarterback

# Create your views here.
def index(request):
    output = ' \n'.join([str(q) for q in Quarterback.objects.all()])
    return HttpResponse(output)
