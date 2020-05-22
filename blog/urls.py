from django.urls import include, path

from blog import views

urlpatterns = [
  path('', views.index),
  path('<slug>', views.post),
]
