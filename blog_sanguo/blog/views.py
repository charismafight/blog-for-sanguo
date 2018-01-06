from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Blog


class Index(ListView):
    model = Blog
    context_object_name = 'blog'

    template_name = 'blog/blog.html'
