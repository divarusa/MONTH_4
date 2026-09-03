from django.http import HttpResponse  # type: ignore[reportMissingModuleSource]
# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello world!</h1>")

def my_name(request):
    name = "Sulamita"
    return HttpResponse(f"<h2> Hello </h2> <h1>{name}</h1>")

def say_name(request, name):
    return HttpResponse(f"<h1>Hello {name}!</h1>")