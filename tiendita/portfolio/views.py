from django.shortcuts import render
from .models import marca
from .models import talla
from .models import departamento
from .models import proveedor
from .models import cliente
from .models import prenda
from .models import venta


# Create your views here.
def portfolio(request):
    marcas = marca.objects.all()
    tallas = talla.objects.all()
    departamentos = departamento.objects.all()
    proveedores = proveedor.objects.all()
    clientes = cliente.objects.all()
    prendas = prenda.objects.all()
    ventas = venta.objects.all()

    return render (request, "portfolio/portfolio.html",{'marcas': marcas, 'tallas': tallas, 'departamentos': departamentos, 'proveedores': proveedores,
    'clientes' : clientes, 'prendas': prendas, 'ventas': ventas})
    