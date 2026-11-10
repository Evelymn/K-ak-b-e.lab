
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Publicacion


User = get_user_model()


class PublicacionPermisosTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear dos usuarias de prueba.
        cls.autora = User.objects.create_user(
            username="autora_test",
            password="ClaveTemporal123!",
            is_staff=True,
        )

        cls.otra_integrante = User.objects.create_user(
            username="integrante_test",
            password="ClaveTemporal456!",
            is_staff=True,
        )

        # Asignar permisos de consulta, edición y eliminación.
        permisos = Permission.objects.filter(
            content_type__app_label="publications",
            codename__in=[
                "view_publicacion",
                "change_publicacion",
                "delete_publicacion",
            ],
        )

        cls.otra_integrante.user_permissions.add(*permisos)

        # Crear una publicación perteneciente a la primera usuaria.
        cls.publicacion = Publicacion.objects.create(
            titulo="Publicación privada de prueba",
            contenido="Contenido para verificar permisos.",
            autora=cls.autora,
            categoria=Publicacion.Categoria.IDEA,
            estado=Publicacion.Estado.BORRADOR,
        )

    def setUp(self):
        # Iniciar sesión como la integrante que NO es autora.
        self.client.force_login(self.otra_integrante)

    def test_no_puede_ver_publicacion_ajena_en_listado(self):
        url = reverse("admin:publications_publicacion_changelist")

        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 200)
        self.assertNotContains(
            respuesta,
            "Publicación privada de prueba",
        )

    def test_no_puede_editar_publicacion_ajena(self):
        url = reverse(
            "admin:publications_publicacion_change",
            args=[self.publicacion.pk],
        )

        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 302)

    def test_no_puede_eliminar_publicacion_ajena(self):
        url = reverse(
            "admin:publications_publicacion_delete",
            args=[self.publicacion.pk],
        )

        respuesta = self.client.get(url)

        self.assertEqual(respuesta.status_code, 302)

        # Comprobar que la publicación sigue existiendo.
        self.assertTrue(
            Publicacion.objects.filter(
                pk=self.publicacion.pk
            ).exists()
          )
def test_no_puede_modificar_publicacion_ajena_por_post(self):
    url = reverse(
        "admin:publications_publicacion_change",
        args=[self.publicacion.pk],
    )

    respuesta = self.client.post(
        url,
        {
            "titulo": "Título modificado sin permiso",
            "contenido": "Intento de modificación",
            "categoria": "idea",
            "estado": "publicada",
            "_save": "Save",
        },
    )

    self.assertIn(respuesta.status_code, [302, 403, 404])

    self.publicacion.refresh_from_db()

    self.assertEqual(
        self.publicacion.titulo,
        "Publicación privada de prueba",
    )

    self.assertEqual(
        self.publicacion.estado,
        "borrador",
    )
