
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Experiencia
from .serializers import ExperienciaSerializer


class ExperienciaListAPIView(generics.ListAPIView):
    """
    API pública de experiencias.

    Devuelve únicamente experiencias publicadas.
    No permite crear, editar ni eliminar registros.
    """

    serializer_class = ExperienciaSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        return (
            Experiencia.objects
            .filter(
                estado=Experiencia.Estado.PUBLICADA
            )
            .select_related(
                "categoria"
            )
            .prefetch_related(
                "fotografias"
            )
            .order_by("-fecha")
        )
