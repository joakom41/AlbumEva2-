from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to="projects", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-created']

    def __str__(self):
        return self.titulo