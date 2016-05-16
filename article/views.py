# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.

def home(request):
    posts = Article.objects.all()
    return render(request, 'home.html', { 'post_list': posts } )
    

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    content_str = "title = {0}, category = {1}, date_time = {2}, content = {3} ".format(post.title, post.category, post.date_time, post.content)
    return HttpResponse(content_str)
    
    
    