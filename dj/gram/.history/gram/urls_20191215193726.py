from django.urls import path
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse()


urlpatterns = [
    path('helloworld', admin.site.urls),
]
