
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Publicacion
from .serializers import PublicacionSerializer


class PublicacionListAPIView(ListAPIView):
    serializer_class = PublicacionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Publicacion.objects.filter(
            estado=Publicacion.Estado.PUBLICADA
        ).select_related('autora')
