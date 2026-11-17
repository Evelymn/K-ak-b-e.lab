
"""
Configuración de rutas principales de k'ak'b'e.lab.

Aquí registramos las rutas de Django Admin,
nuestras API REST y los archivos multimedia
durante el desarrollo.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Rutas principales de nuestra aplicación.
urlpatterns = [
    path('admin/', admin.site.urls),

    # API REST de publicaciones.
    path('api/publicaciones/', include('publications.urls')),
]


# Servir fotografías subidas durante el desarrollo.
# Este mecanismo no debe utilizarse en producción.
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
