from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


SEXO = [
        ("F", "Femenino"),
        ("M", "Masculino"),
        ("O", "Otro"),
    ]

class User(AbstractUser):
    pass 

class Familiar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut=models.CharField(primary_key=True, null=False, max_length=10,error_messages="Debe ingresar rut")
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    f_nacimiento=models.DateField()
    n_telefono=models.CharField(max_length=15)
    email=models.EmailField()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
class Aportador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    nro_tarjeta = models.IntegerField(max_length=16)
    sexo=models.CharField(max_length=1, choices=SEXO)


    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Residente(models.Model):
    rut=models.CharField(primary_key=True, null=False, max_length=10,error_messages="Debe ingresar rut")
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    f_nacimiento=models.DateField()
    sexo=models.CharField(max_length=1, choices=SEXO)
    tutor=models.ForeignKey(Familiar, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Accion(models.Model):  #La acción que realiza la enfermera o cuidador al
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    descripcion = models.TextField()

class Insumo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)+' ID: '+(self.id)

class CompraInsumo(models.Model):
    fecha_compra = models.DateField()
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=40)
    costo_unitario = models.IntegerField()
    

    def __str__(self):
        return str(self.fecha_compra)+' - '+str(self.insumo)
    
class StockInsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad_stock = models.IntegerField()

    def __str__(self):
        return str(self.insumo) + ' - ' + str(self.cantidad_stock)
    
class Staff:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()