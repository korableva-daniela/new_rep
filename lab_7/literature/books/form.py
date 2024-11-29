from .models import Book, Author
from django import forms
from django.forms import ModelForm, TextInput


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'second_name', 'email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'content', 'status']
