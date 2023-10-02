from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'input'}),
            'email' : forms.EmailInput(attrs={'class': 'input'}),
            'body' : forms.Textarea(attrs={'class': 'textarea', 'rows': '3'}),
        }
