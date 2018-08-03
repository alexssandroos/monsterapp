from django.contrib import admin
from .models import Modalidade, Turma, Horario

# Register your models here.
admin.site.register(Modalidade)
admin.site.register(Turma)
admin.site.register(Horario)
