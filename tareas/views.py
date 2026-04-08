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
    contactos = Usuario.objects.all()

    if request.method == "POST":
        contacto_id = request.POST.get("contacto")
        monto = request.POST.get("monto")
        tipo = request.POST.get("tipo")

        contacto = Usuario.objects.get(id=contacto_id)

        Transaccion.objects.create(usuario=contacto, monto=monto, tipo=tipo)

        return redirect("lista")

    return render(request, "form.html", {"contactos": contactos})


def editar_transaccion(request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    contactos = Usuario.objects.all()

    if request.method == "POST":
        contacto_id = request.POST.get("contacto")
        monto = request.POST.get("monto")
        tipo = request.POST.get("tipo")

        contacto = Usuario.objects.get(id=contacto_id)

        transaccion.usuario = contacto
        transaccion.monto = monto
        transaccion.tipo = tipo
        transaccion.save()

        return redirect("lista")

    return render(
        request, "form.html", {"transaccion": transaccion, "contactos": contactos}
    )


def eliminar_transaccion(request, id):
    transaccion = get_object_or_404(Transaccion, id=id)
    transaccion.delete()
    return redirect("lista")


def crear_contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        Usuario.objects.create(nombre=nombre)
        return redirect("lista")

    return render(request, "crear_contacto.html")


def detalle_contacto(request, id):
    contacto = get_object_or_404(Usuario, id=id)
    transacciones = Transaccion.objects.filter(usuario=contacto)

    ingresos = sum(t.monto for t in transacciones if t.tipo == "ingreso")
    gastos = sum(t.monto for t in transacciones if t.tipo == "gasto")
    saldo = ingresos - gastos

    return render(
        request,
        "detalle_contacto.html",
        {
            "contacto": contacto,
            "transacciones": transacciones,
            "ingresos": ingresos,
            "gastos": gastos,
            "saldo": saldo,
        },
    )
