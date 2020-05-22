from django.shortcuts import render

from blog.models import BlogPage, PostPage

def index(request):
  page = BlogPage.objects.get()
  return page.render(request)

def post(request, slug):
  page = PostPage.objects.get()
  return page.render(request, slug=slug)

