from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'helloworld/hello_world.html')