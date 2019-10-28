from django.contrib import admin
# Register your models here.
from .models import Turma, Curso, Professor

class TurmaInline(admin.TabularInline):
    model = Turma

class ProfessorAdmin(admin.ModelAdmin):
    inlines = [
        TurmaInline,
    ]
    class Meta:
        model = Turma

admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Professor, ProfessorAdmin)

