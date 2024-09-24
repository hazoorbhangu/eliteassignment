from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

from mainapp.models import QuoteRequest
from .forms import ContactForm, QuoteForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Save the form data to the model
            QuoteRequest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                service=form.cleaned_data['service'],
                message=form.cleaned_data['message']
            )
            
            # Optionally send an email
            # send_mail(
            #     f'Quote Request from {form.cleaned_data["name"]}',
            #     f'Service: {form.cleaned_data["service"]}\n\nMessage: {form.cleaned_data["message"]}',
            #     'your_email@example.com',
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )
            messages.success(request, 'Your quote request has been submitted successfully!')

            
    else:
        form = QuoteForm()
    
    return render(request,"index.html",locals())

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
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Save the form data to the model
            QuoteRequest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                service=form.cleaned_data['service'],
                message=form.cleaned_data['message']
            )
            
            # Optionally send an email
            # send_mail(
            #     f'Quote Request from {form.cleaned_data["name"]}',
            #     f'Service: {form.cleaned_data["service"]}\n\nMessage: {form.cleaned_data["message"]}',
            #     'your_email@example.com',
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )
            messages.success(request, 'Your quote request has been submitted successfully!')

            
    else:
        form = QuoteForm()
    
    return render(request,"quote.html",locals())


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the model
            QuoteRequest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                service=form.cleaned_data['service'],
                message=form.cleaned_data['message']
            )
            
            # Optionally send an email
            # send_mail(
            #     f'Quote Request from {form.cleaned_data["name"]}',
            #     f'Service: {form.cleaned_data["service"]}\n\nMessage: {form.cleaned_data["message"]}',
            #     'your_email@example.com',
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )
            messages.success(request, 'Your quote request has been submitted successfully!')

            
    else:
        form = ContactForm()
    
    return render(request,"contact.html",locals())