from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class marca(models.Model):
    idmarca = models.IntegerField(primary_key=True,verbose_name = "Codigo de la marca")
    marca = models.CharField(max_length=40,verbose_name= "Nombre de la marca")
    imagen = models.ImageField(verbose_name= "imagen", upload_to= "img_marcas")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class talla(models.Model):
    idtalla = models.IntegerField(primary_key=True,verbose_name = "Codigo de la talla")
    talla = models.CharField(max_length= 3, verbose_name= "Talla")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class departamento(models.Model):
    iddepartamento = models.IntegerField(primary_key=True,verbose_name= "Codigo departamento")
    nomDepartamento = models.CharField(max_length= 10, verbose_name= "Nombre del departamento")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class proveedor(models.Model):
    idproveedor = models.IntegerField(primary_key=True,verbose_name="Codigo proveedor")
    nomProveedor = models.CharField(max_length= 15, verbose_name="Nombre del proveedor")
    telefono = models.CharField(max_length= 13, verbose_name="Numero de telefono")
    correo = models.TextField(verbose_name="e-mail")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class cliente(models.Model):
    idcliente = models.IntegerField(primary_key=True,verbose_name="Codigo de cliente")
    usuario = models.CharField(max_length=20, verbose_name="usuario")
    correo = models.TextField(verbose_name="e-mail")
    contraseña = models.CharField(max_length=8, verbose_name="contraseña")
    nomCliente = models.CharField(max_length = 40, verbose_name="Nombre del cliente")
    direccion = models.CharField(max_length= 100, verbose_name="Dirrecion")
    telefono = models.CharField(max_length=13, verbose_name="Numero de telefono")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class prenda(models.Model):
    marca = models.ForeignKey(marca, on_delete= models.CASCADE)
    talla = models.ForeignKey(talla,on_delete= models.CASCADE)
    departamento = models.ForeignKey(departamento,on_delete= models.CASCADE)
    proveedor = models.ForeignKey(proveedor,on_delete= models.CASCADE)
    idprenda = models.IntegerField(primary_key=True,verbose_name= "codigo de la prenda")
    precio = models.FloatField(verbose_name="precio de la prenda")
    cantidad = models.IntegerField(verbose_name="cantidad a comprar")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")

class venta(models.Model):
    cliente = models.ForeignKey(cliente,on_delete= models.CASCADE)
    prenda = models.ForeignKey(prenda,on_delete= models.CASCADE)
    idventa = models.IntegerField(primary_key=True,verbose_name="codigo de venta")
    fecha = models.DateTimeField(verbose_name="fecha de la compra")
    create = models.DateField(auto_now_add= True,verbose_name= "Fecha de creacion")
    update = models.DateField(auto_now= True,verbose_name= "Fecha edicion")




class Meta:
    verbose_name = "marca"
    verbose_name_plural = "marcas"
    ordering = ["-created"]