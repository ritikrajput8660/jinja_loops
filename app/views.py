from django.shortcuts import render
# Create your views here.

def checkNum(request):
    
    d={'name':'RITIK','age':25,'gender':'male'}
    return render(request,'index.html',d)
