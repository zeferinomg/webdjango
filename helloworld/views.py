from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def hello_world(request):
    return render(request, 'helloworld/hello_world.html')