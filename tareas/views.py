from django.shortcuts import render, redirect
from .models import Transaccion
from .forms import TransaccionForm


def lista_transacciones(request):
    query = request.GET.get("q")

    transacciones = Transaccion.objects.all()

    if query:
        transacciones = transacciones.filter(usuario__nombre__icontains=query)

    return render(request, "lista.html", {"transacciones": transacciones})


def crear_transaccion(request):
    form = TransaccionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista")
    return render(request, "form.html", {"form": form})


def editar_transaccion(request, id):
    transaccion = Transaccion.objects.get(id=id)
    form = TransaccionForm(request.POST or None, instance=transaccion)
    if form.is_valid():
        form.save()
        return redirect("lista")
    return render(request, "form.html", {"form": form})


def eliminar_transaccion(request, id):
    transaccion = Transaccion.objects.get(id=id)
    transaccion.delete()
    return redirect("lista")
