from django.db import models

# Create your models here.

# SAP_COD_CLASE

class Clase(models.Model): 
    cod_clase = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self): # ------------------------------------------->>>> el str define como se mostrara el objeto o que se vera en el Admin de Django.
        return f'{self.cod_clase} - {self.nombre} '


# ********************************************************************
# SAP_COD_MARCA

class Marca(models.Model): 
    cod_marca = models.IntegerField(max_length=10, unique=True)
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
    # ForeignKey → esto habilita el <select> con las opciones ya cargadas
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT, related_name='modelos') 
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='modelos')
    descripcion = models.CharField(max_length=200, blank=True)
    cod_veh = models.IntegerField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='modelo', blank=True, null=True)
    
    def __str__(self):
        return f'{self.cod_modelo} - {self.clase}- {self.marca} - {self.cod_veh} - {self.descripcion or 'Sin desc.'}'


# ********************************************************************

# SAP_PARTES (puerta, faro, paragolpes…)

class Parte(models.Model):
    cod_parte = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.cod_parte} - {self.nombre}'

# ********************************************************************

# SAP_ELEMENTOS (granularidad debajo de Parte)

class Elemento(models.Model):  
    cod_elemento = models.CharField(max_length=20)
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT, related_name="elementos")
    parte = models.ForeignKey(Parte, on_delete=models.PROTECT, related_name="elementos")
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='elemento', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.cod_elemento} - {self.nombre}"
