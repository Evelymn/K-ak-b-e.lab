
from django.urls import path

from .views import ExperienciaListAPIView


urlpatterns = [
    path(
        "",
        ExperienciaListAPIView.as_view(),
        name="experiencia-list"
    ),
]
