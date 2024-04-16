from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def product_list(request):
    productes = Producto.objects.all()

    # Devolver la lista de productos como una respuesta JSON
    return JsonResponse(list(productos), safe=False)