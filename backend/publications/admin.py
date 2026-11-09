
# Register your models here.
from django.contrib import admin
from .models import Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'autora',
        'categoria',
        'estado',
        'fecha_creacion',
    )

    list_filter = (
        'categoria',
        'estado',
    )

    search_fields = (
        'titulo',
        'contenido',
        'autora__username',
    )

    readonly_fields = (
        'fecha_creacion',
        'fecha_actualizacion',
    )

     # Mostrar solo las publicaciones propias
    # a quienes no sean superusuarios.
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(autora=request.user)

    # Comprobar permisos de edición.
    def has_change_permission(self, request, obj=None):
        if not super().has_change_permission(request, obj):
            return False

        if obj is None or request.user.is_superuser:
            return True

        return obj.autora_id == request.user.pk

    # Comprobar permisos de eliminación.
    def has_delete_permission(self, request, obj=None):
        if not super().has_delete_permission(request, obj):
            return False

        if obj is None or request.user.is_superuser:
            return True

        return obj.autora_id == request.user.pk

    # La autora no debe modificarse manualmente
    # desde el formulario.
    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_exclude(request, obj)

        return ('autora',)

    # Asignar automáticamente la autora
    # al crear una publicación.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.autora = request.user

        super().save_model(request, obj, form, change)
