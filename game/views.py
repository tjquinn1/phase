from django.http import HttpResponseRedirect
from django.shortcuts import render



def index(request):
    return render(request, 'index.html', {})

def solitaire(request):
    return render(request, 'solitaire.html', {})