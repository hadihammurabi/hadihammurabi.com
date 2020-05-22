from django.shortcuts import render

from blog.models import BlogPage, PostPage

def index(request):
  page = BlogPage.objects.get()
  return page.render(request)

def post(request, slug):
  page = PostPage.objects.filter(slug=slug).first()
  return render(request, 'blog/post_page.html', context={'post': page})


