
from rest_framework import serializers
from .models import Publicacion


class PublicacionSerializer(serializers.ModelSerializer):
    autora = serializers.CharField(
        source='autora.username',
        read_only=True
    )

    class Meta:
        model = Publicacion
        fields = [
            'id',
            'titulo',
            'contenido',
            'autora',
            'categoria',
            'estado',
            'fecha_creacion',
        ]
