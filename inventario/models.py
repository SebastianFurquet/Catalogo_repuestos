from django.db import models

# Create your models here.

# SAP_COD_CLASE

class Clase(models.Model): 
    cod_clase = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self): # ------------------------------------------->>>> el str define como se mostrara el objeto o que se vera en el Admin de Django.
        return f'{self.cod_clase} - {self.nombre} - {self.fecha_creacion} - {self.fecha_modificacion} '


# ********************************************************************
# SAP_COD_MARCA

class Marca(models.Model): 
    cod_marca = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='marca', null=True)
    
    def __str__(self):
        return f'{self.cod_marca} - {self.nombre}'
    
# ********************************************************************

# LPM_CODIGOS_POLARIS_TIPO_VEH (la parte de modelo).
# codificacion de modelos 
# Cada descripcion del modelo se construye con cod_clase /cod_marca/ cod_modelo

# models.ForeignKey: establece la relacion entre tablas en base a un campo
# on_delete=models.PROTECT : si alguien intenta borrar una Clase que tiene Elementos asociados, Django no permitira borrarla (Proteccion)
# related_name='modelos': permite acceder desde una instancia de Clase a todos sus elementos con clase.elementos.all()


class Modelo(models.Model):
    cod_modelo = models.IntegerField(max_length=20)
    clase = models.IntegerField(max_length=10) 
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True)
    cod_veh = models.IntegerField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='modelo ', null=True)
    
    def __str__(self):
        return f'{self.cod_modelo} - {self.cod_veh} - {self.descripcion or 'Sin desc.'}'