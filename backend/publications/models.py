from django.conf import settings
from django.db import models


class Publicacion(models.Model):

    # Categorías disponibles
    class Categoria(models.TextChoices):
        IDEA = 'idea', 'Idea'
        NOTICIA = 'noticia', 'Noticia'
        EXPERIENCIA = 'experiencia', 'Experiencia'
        REFLEXION = 'reflexion', 'Reflexión'

    # Estados de publicación
    class Estado(models.TextChoices):
        BORRADOR = 'borrador', 'Borrador'
        PUBLICADA = 'publicada', 'Publicada'

    # Información principal
    titulo = models.CharField(max_length=200)

    contenido = models.TextField()

    autora = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='publicaciones'
    )

    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.IDEA
    )

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.BORRADOR
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo
