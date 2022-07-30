from django.shortcuts import render

def vista (request):
    return render (request,"plantillaPadre.html",context={})