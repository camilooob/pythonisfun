from django.urls import path
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hola mama")


urlpatterns = [
    path('helloworld/',helloworld)
]
