### views.py ###
from django.shortcuts import render

# no context is needed, omit the 3rd param


def home(request):
    return render(request, 'home.html')
