from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json

def showProducts(request):
    jsonData = list( Producto.objects.all().values() )
    return JsonResponse ({
        "status" : "OK",
        "productes" : jsonData,
    } ,safe = False)

def showProduct(request, id_prod):
    product = Producto.objects.get(id=id_prod)
    product_data = {
        'id': product.id,
        'nombre': product.nombre,
        'descripcion': product.descripcion,
        'precio': product.precio
    }
    return JsonResponse ({
        "status" : "OK",
        "productes" : product_data,
    }, safe = False)

@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del producto del cuerpo de la solicitud POST
            data = json.loads(request.body)
            
            # Crear un nuevo producto con los datos proporcionados
            nuevo_producto = Producto(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'])
            
            # Guardar el nuevo producto en la base de datos
            nuevo_producto.save()
            
            # Devolver una respuesta JSON indicando que el producto fue añadido con éxito
            return JsonResponse({'mensaje': 'Producto añadido correctamente'}, status=201)  # 201 significa "Created"
        except KeyError:
            # Si faltan campos en los datos recibidos, devolver un mensaje de error
            return JsonResponse({'mensaje': 'Datos de producto incompletos'}, status=400)  # 400 significa "Bad Request"
    else:
        # Devolver un mensaje de error si el método de solicitud no es POST
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)  # 405 significa "Method Not Allowed"

@csrf_exempt
def deleteProduct(request, id):
    try:
        # Obtener el producto por su ID
        producto = Producto.objects.get(pk=id)
        
        # Eliminar el producto
        producto.delete()
        
        # Devolver una respuesta JSON indicando que el producto fue eliminado con éxito
        return JsonResponse({'mensaje': 'Producto eliminado correctamente'}, status=204)  # 204 significa "No Content"
    except Producto.DoesNotExist:
        # Si el producto no existe, devolver un mensaje de error
        return JsonResponse({'mensaje': 'El producto no existe'}, status=404)  # 404 significa "Not Found"
