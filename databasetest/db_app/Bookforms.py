from django import forms
from .models import Book
from django.shortcuts import render, redirect

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        

