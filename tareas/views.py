from django.shortcuts import render, redirect
from .models import Transaccion
from .forms import TransaccionForm, UsuarioForm


def lista_transacciones(request):
    query = request.GET.get("q")

    if query:
        transacciones = Transaccion.objects.filter(usuario__nombre__icontains=query)
    else:
        transacciones = Transaccion.objects.all()

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


def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista")
    return render(request, "usuario_form.html", {"form": form})
