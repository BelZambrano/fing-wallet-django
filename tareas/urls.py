from django.urls import path
from .views import lista_transacciones, crear_transaccion
from .views import editar_transaccion, eliminar_transaccion

urlpatterns = [
    path("", lista_transacciones, name="lista"),
    path("crear/", crear_transaccion, name="crear"),
    path("editar/<int:id>/", editar_transaccion, name="editar"),
    path("eliminar/<int:id>/", eliminar_transaccion, name="eliminar"),
]
