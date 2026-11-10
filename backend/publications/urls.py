from django.urls import path
from .views import PublicacionListAPIView

urlpatterns = [
    path(
        '',
        PublicacionListAPIView.as_view(),
        name='publicaciones-list'
    ),
]
