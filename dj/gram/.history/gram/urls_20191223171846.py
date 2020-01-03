from django.urls import path
from gram import pages as local_pages
from posts import views as posts_pages

urlpatterns = [
    path('helloworld/', local_pages.helloworld)
    path('posts/', posts_pages.list_posts)
]
