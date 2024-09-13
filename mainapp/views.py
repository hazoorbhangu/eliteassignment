from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def service(request):
    return render(request,"service.html")


def blog(request):
    return render(request,"blog.html")


def detail(request):
    return render(request,"detail.html")

def price(request):
    return render(request,"price.html")


def feature(request):
    return render(request,"feature.html")

def team(request):
    return render(request,"team.html")

def testimonial(request):
    return render(request,"testimonial.html")

def quote(request):
    return render(request,"quote.html")


def contact(request):
    return render(request,"contact.html")