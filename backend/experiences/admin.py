
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.contrib import admin
from .models import CategoriaExperiencia, Experiencia, FotoExperiencia


class FotoExperienciaFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()

        # Si hay errores en los formularios individuales,
        # no continuamos con esta validación.
        if any(self.errors):
            return

        total = 0

        for form in self.forms:

            # Ignoramos formularios vacíos o eliminados.
            if not form.cleaned_data:
                continue

            if form.cleaned_data.get("DELETE", False):
                continue

            total += 1

        if total > 4:
            raise ValidationError(
                "Una experiencia no puede tener "
                "más de 4 fotografías."
            )


class FotoExperienciaInline(admin.TabularInline):
    formset = FotoExperienciaFormSet
    model = FotoExperiencia

    # No mostrar formularios vacíos por defecto.
    extra = 0

    # Número máximo de formularios del inline.
    max_num = 4

    # Campos que se mostrarán.
    fields = (
        "imagen",
        "texto_alternativo",
        "orden",
    )

@admin.register(Experiencia)

class ExperienciaAdmin(admin.ModelAdmin):
    inlines = [FotoExperienciaInline]

    # Columnas visibles en el listado.
    list_display = (
        "titulo",
        "categoria",
        "responsable",
        "fecha",
        "estado",
    )

    # Filtros laterales.
    list_filter = (
        "categoria",
        "estado",
        "fecha",
    )

    # Permite buscar experiencias.
    search_fields = (
        "titulo",
        "descripcion",
    )

    # Ordena las experiencias por fecha.
    ordering = ("-fecha",)

    # El responsable se asignará automáticamente
    # desde el usuario autenticado.
    readonly_fields = (
        "fecha_creacion",
    )

    # Campos visibles en el formulario.
    fields = (
        "titulo",
        "descripcion",
        "fecha",
        "categoria",
        "estado",
        "fecha_creacion",
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.responsable = request.user

        super().save_model(request, obj, form, change)


    # Columnas visibles en el listado.
    list_display = (
        "nombre",
        "slug",
    )

    # Permite buscar categorías por nombre.
    search_fields = (
        "nombre",
    )

    # Genera una sugerencia de slug a partir del nombre.
    prepopulated_fields = {
        "slug": ("nombre",)
    }

    # Ordena las categorías alfabéticamente.
    ordering = ("nombre",)
