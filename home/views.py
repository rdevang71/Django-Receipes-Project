from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples = [
            {'name':'Devang Rajput','age':21},
            {'name':'Shushant Rajput','age':19},
            {'name':'Daksh Rajput','age':16},
            {'name':'Chirag Rajput','age':19},
        ]
    return render(request, "index.html", context = {'peoples':peoples})

def about(request):
    return render(request ,"about.html")

def contact(request):
    return render(request ,"contact.html")