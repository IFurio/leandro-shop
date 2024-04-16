from django.urls import path
from . import views, api

urlpatterns = [
    path("api/addProduct", api.addProduct),
    path("api/deleteProduct/<int:id>", api.deleteProduct),
    path("api/showProducts", api.showProducts),
    path("api/showProduct/<int:id_prod>", api.showProduct),
]
