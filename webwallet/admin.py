from django.contrib import admin
from .models import Carteira, Ativo, Acao, Relatorio

# Register your models here.

admin.site.register(Carteira)
admin.site.register(Ativo)
admin.site.register(Acao)
admin.site.register(Relatorio)
admin.site.register(Cadastro)
