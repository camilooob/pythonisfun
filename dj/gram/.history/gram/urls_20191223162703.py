from django.urls import path
from gram import pages

urlpatterns = [
    path('helloworld/', pages.helloworld)
]
