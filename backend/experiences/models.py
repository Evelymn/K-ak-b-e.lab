
from django.db import models
from django.core.exceptions import ValidationError


class CategoriaExperiencia(models.Model):
    # Nombre visible de la categoría.
    # Ejemplos: Talleres, Competencias, Cursos.
    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    # Identificador legible para las URL.
    # Ejemplo: "Competencias" -> "competencias".
    slug = models.SlugField(
        max_length=120,
        unique=True
    )

    class Meta:
        verbose_name = "Categoría de experiencia"
        verbose_name_plural = "Categorías de experiencias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Experiencia(models.Model):

    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        PUBLICADA = "publicada", "Publicada"

    titulo = models.CharField(
        max_length=200
    )

    descripcion = models.TextField()

    fecha = models.DateField()

    categoria = models.ForeignKey(
        CategoriaExperiencia,
        on_delete=models.PROTECT,
        related_name="experiencias"
    )

    responsable = models.ForeignKey(
        "accounts.User",
        on_delete=models.PROTECT,
        related_name="experiencias_registradas"
    )

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.BORRADOR
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

class FotoExperiencia(models.Model):

    experiencia = models.ForeignKey(
        Experiencia,
        on_delete=models.CASCADE,
        related_name="fotografias"
    )

    imagen = models.ImageField(
        upload_to="experiencias/"
    )

    texto_alternativo = models.CharField(
        max_length=200
    )

    orden = models.PositiveSmallIntegerField(
        default=1
    )

    class Meta:
        verbose_name = "Fotografía de experiencia"
        verbose_name_plural = "Fotografías de experiencias"
        ordering = ["orden", "id"]

    def __str__(self):
        return f"Foto {self.orden} - {self.experiencia.titulo}"

    def clean(self):
        super().clean()

        if not self.experiencia_id:
            return

        fotografias = FotoExperiencia.objects.filter(
            experiencia_id=self.experiencia_id
        )

        # Si editamos una fotografía, no la contamos
        # como si fuera una fotografía nueva.
        if self.pk is not None:
            fotografias = fotografias.exclude(pk=self.pk)

        if fotografias.count() >= 4:
            raise ValidationError({
                "experiencia": (
                    "Una experiencia no puede tener "
                    "más de 4 fotografías."
                )
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

