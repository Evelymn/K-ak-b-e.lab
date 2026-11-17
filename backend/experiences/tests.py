
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import (
    CategoriaExperiencia,
    Experiencia,
    FotoExperiencia,
)


class FotoExperienciaTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        cls.usuario = User.objects.create_user(
            username="usuario_prueba",
            password="PasswordSegura123!"
        )

        cls.categoria = CategoriaExperiencia.objects.create(
            nombre="Competencias",
            slug="competencias"
        )

        cls.experiencia = Experiencia.objects.create(
            titulo="Hackathon de prueba",
            descripcion="Experiencia para probar fotografías.",
            fecha="2026-09-15",
            categoria=cls.categoria,
            responsable=cls.usuario
        )

    def crear_foto(self, orden):
        return FotoExperiencia.objects.create(
            experiencia=self.experiencia,
            imagen=SimpleUploadedFile(
                f"foto_{orden}.jpg",
                b"contenido-de-prueba",
                content_type="image/jpeg"
            ),
            texto_alternativo=f"Fotografía {orden}",
            orden=orden
        )

    def test_permite_cuatro_fotografias(self):
        for numero in range(1, 5):
            self.crear_foto(numero)

        total = FotoExperiencia.objects.filter(
            experiencia=self.experiencia
        ).count()

        self.assertEqual(total, 4)

    def test_rechaza_quinta_fotografia(self):
        for numero in range(1, 5):
            self.crear_foto(numero)

        with self.assertRaises(ValidationError):
            self.crear_foto(5)

        self.assertEqual(
            self.experiencia.fotografias.count(),
            4
        )

    def test_permite_editar_fotografia_existente(self):
        for numero in range(1, 5):
            self.crear_foto(numero)

        foto = self.experiencia.fotografias.first()
        foto.texto_alternativo = "Descripción actualizada"
        foto.save()

        foto.refresh_from_db()

        self.assertEqual(
            foto.texto_alternativo,
            "Descripción actualizada"
        )
