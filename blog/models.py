from django.db import models
from django.utils import timezone

#se crea el modelo adoptante 

class Adoptantes(models.Model):
        Correo = models.EmailField(null=False)
        Rut = models.CharField(null=False  , max_length=9)
        NombreCompleto = models.CharField(max_length=30, null=False)
        FechaNacimiento = models.DateField(null=False)
        Telefono = models.IntegerField(null=False)
        Region = models.IntegerField(null=False)
        Ciudad = models.IntegerField(null=False)
        VIVIENDAS = (('casa2','Casa con patio Grande'),('casa3','Casa con patio pequeño'),('casa4','Casa sin patio'),('casa5','Departamento'))
        TipoVivienda = models.CharField(max_length=1 ,choices=VIVIENDAS , null=False, default='casa2')

#se crea el modelo del registro rescatados 

class RegistroRescatados(models.Model):
        Nombre = models.CharField(max_length=20, null=False)
        Fotografia = models.ImageField(null=False)
        RazaPredominante = models.CharField(max_length=20, null=False)
        Descripcion = models.TextField(null=False)
        ESTADOS = (('R','Rescatados'),('D','Disponible'),('A','Adoptado'))
        Estado = models.CharField(max_length=1 ,choices=ESTADOS , null=False, default='D')

        def __str__(self):
            return self.Nombre


        

        


