from django.shortcuts import render

def home(reuest): 
    template = "home.html"
    context = {} # what are wee sending back to the page
    return render(request, template, context)

