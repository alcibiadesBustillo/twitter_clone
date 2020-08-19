from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

import sys
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
