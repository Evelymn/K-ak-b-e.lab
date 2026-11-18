
from rest_framework import serializers

from .models import Experiencia, FotoExperiencia


class FotoExperienciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FotoExperiencia
        fields = [
            "id",
            "imagen",
            "texto_alternativo",
            "orden",
        ]


class ExperienciaSerializer(serializers.ModelSerializer):

    categoria = serializers.CharField(
        source="categoria.nombre",
        read_only=True
    )

    fotografias = FotoExperienciaSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Experiencia
        fields = [
            "id",
            "titulo",
            "descripcion",
            "fecha",
            "categoria",
            "fotografias",
        ]
