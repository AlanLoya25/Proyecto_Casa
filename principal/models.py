from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Casa(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    habitaciones = models.PositiveIntegerField(default=1)
    banos = models.PositiveIntegerField(default=1)
    metros_cuadrados = models.PositiveIntegerField(default=50)
    imagen = models.ImageField(upload_to='casas/', null=True, blank=True)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Opinion(models.Model):
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='opiniones')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.casa.titulo}"

class Promocion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de descuento")
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name="promociones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    creado_por = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.descuento}%"
