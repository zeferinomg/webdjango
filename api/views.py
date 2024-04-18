import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_prueba(request):
    if request.method == 'GET':
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'mocks/results.json')
            print("Ruta del archivo:", file_path)  # Depuración: imprime la ruta del archivo
            with open(file_path) as f:
                data = json.load(f)
            return JsonResponse(data)
        except FileNotFoundError:
            return JsonResponse({'error': 'El archivo no se encontró'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'No se pudo decodificar el JSON'})
