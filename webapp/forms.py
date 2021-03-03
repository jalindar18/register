from django.contrib.auth.admin import User
from .models import Blog
from django import forms


class Register_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username','password','email']

class Blog_Form(forms.ModelForm):

    class Meta:

        model = Blog
        fields = ['title','subject','blog_text']

