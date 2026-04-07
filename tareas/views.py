from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaccion, Usuario


def lista_transacciones(request):
    query = request.GET.get("q")

    transacciones = Transaccion.objects.all()

    if query:
        transacciones = transacciones.filter(usuario__nombre__icontains=query)

    ingresos = sum(t.monto for t in transacciones if t.tipo == "ingreso")
    gastos = sum(t.monto for t in transacciones if t.tipo == "gasto")
    saldo = ingresos - gastos

    return render(
        request,
        "lista.html",
        {
            "transacciones": transacciones,
            "ingresos": ingresos,
            "gastos": gastos,
            "saldo": saldo,
        },
    )


def crear_transaccion(request):
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        usuario_id = request.POST.get("usuario")
        monto = request.POST.get("monto")
        tipo = request.POST.get("tipo")

        usuario = Usuario.objects.get(id=usuario_id)

        Transaccion.objects.create(usuario=usuario, monto=monto, tipo=tipo)

        return redirect("lista")

    return render(request, "form.html", {"usuarios": usuarios})


def editar_transaccion(request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    usuarios = Usuario.objects.all()

    if request.method == "POST":
        transaccion.usuario_id = request.POST.get("usuario")
        transaccion.monto = request.POST.get("monto")
        transaccion.tipo = request.POST.get("tipo")
        transaccion.save()

        return redirect("lista")

    return render(
        request, "form.html", {"transaccion": transaccion, "usuarios": usuarios}
    )


def eliminar_transaccion(request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    transaccion.delete()
    return redirect("lista")


def crear_usuario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        Usuario.objects.create(nombre=nombre)
        return redirect("lista")

    return render(request, "crear_usuario.html")
