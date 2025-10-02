from django.db import models

class ObraArte(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    artista = models.CharField(max_length=150, verbose_name="Artista")
    year = models.CharField(max_length=50, verbose_name="Año", blank=True, null=True)
    tecnica = models.CharField(max_length=200, verbose_name="Técnica")
    dimensiones = models.CharField(max_length=100, verbose_name="Dimensiones")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to="obras/", verbose_name="Imagen de la Obra")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Obra de Arte"
        verbose_name_plural = "Obras de Arte"
        ordering = ['-created']

    def __str__(self):
        return f"{self.titulo} - {self.artista}"