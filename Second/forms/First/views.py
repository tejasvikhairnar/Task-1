from django.shortcuts import render
from .models import ChaiVarity

def first_file(request):
    chais = ChaiVarity.objects.all()
    return render(request,'first.html', {'chais': chais})

# Create your views here.
