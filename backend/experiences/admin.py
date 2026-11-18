
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import CategoriaExperiencia, Experiencia, FotoExperiencia


# ==========================================
# ADMINISTRACIÓN DE CATEGORÍAS
# ==========================================

@admin.register(CategoriaExperiencia)
class CategoriaExperienciaAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
        "slug",
    )

    search_fields = (
        "nombre",
    )

    prepopulated_fields = {
        "slug": ("nombre",)
    }

    ordering = ("nombre",)


# ==========================================
# VALIDACIÓN DE FOTOGRAFÍAS
# ==========================================

class FotoExperienciaFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()

        if any(self.errors):
            return

        total = 0

        for form in self.forms:

            # Ignorar formularios vacíos.
            if not form.cleaned_data:
                continue

            # Ignorar fotografías eliminadas.
            if form.cleaned_data.get("DELETE", False):
                continue

            total += 1

        if total > 4:
            raise ValidationError(
                "Una experiencia no puede tener "
                "más de 4 fotografías."
            )


# ==========================================
# FOTOGRAFÍAS DENTRO DE EXPERIENCIAS
# ==========================================

class FotoExperienciaInline(admin.TabularInline):

    model = FotoExperiencia
    formset = FotoExperienciaFormSet

    extra = 0
    max_num = 4

    fields = (
        "imagen",
        "texto_alternativo",
        "orden",
    )


# ==========================================
# ADMINISTRACIÓN DE EXPERIENCIAS
# ==========================================

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):

    inlines = [FotoExperienciaInline]

    list_display = (
        "titulo",
        "categoria",
        "responsable",
        "fecha",
        "estado",
    )

    list_filter = (
        "categoria",
        "estado",
        "fecha",
    )

    search_fields = (
        "titulo",
        "descripcion",
    )

    ordering = ("-fecha",)

    readonly_fields = (
        "fecha_creacion",
    )

    fields = (
        "titulo",
        "descripcion",
        "fecha",
        "categoria",
        "estado",
        "fecha_creacion",
    )

    def save_model(self, request, obj, form, change):

        # Asignar automáticamente el responsable
        # al crear una experiencia.
        if not change:
            obj.responsable = request.user

        super().save_model(request, obj, form, change)
