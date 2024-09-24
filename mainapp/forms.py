

# forms.py
from django import forms

class QuoteForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control bg-light border-0', 
        'placeholder': 'Your Name',
        'style':'height:55px'

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control bg-light border-0', 
        'placeholder': 'Your Email',
        'style':'height:55px'

    }))
    service = forms.ChoiceField(choices=[
        ('Assignments', 'Assignments'),
        ('Thesis', 'Thesis'),
        ('Others', 'Others')
    ], widget=forms.Select(attrs={
        'class': 'form-select bg-light border-0',   
        'style':'height:55px'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control bg-light border-0', 
        'placeholder': 'Message',
        'rows':'3'
    }))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control border-0 bg-light px-4', 
        'placeholder': 'Your Name',
        'style':'height:55px'

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control border-0 bg-light px-4', 
        'placeholder': 'Your Email',
        'style':'height:55px'

    }))
    service = forms.ChoiceField(choices=[
        ('Assignments', 'Assignments'),
        ('Thesis', 'Thesis'),
        ('Others', 'Others')
    ], widget=forms.Select(attrs={
        'class': 'form-control border-0 bg-light px-4',   
        'style':'height:55px'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control border-0 bg-light px-4 py-3', 
        'placeholder': 'Message',
        'rows':'4'
    }))
