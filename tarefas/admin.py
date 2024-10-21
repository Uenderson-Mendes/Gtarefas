from django.contrib import admin
from .models import Usuario, CadastroTarefas

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_user', 'is_staff', 'is_superuser', 'is_active')  # Campos que você quer ver na listagem
    search_fields = ('cpf', 'nome_user')  # Campos para buscar usuários
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # Filtros para os usuários
    ordering = ('cpf',)  # Ordenação por CPF
    fieldsets = (
        (None, {'fields': ('cpf', 'nome_user', 'senha')}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'nome_user', 'senha1', 'senha2'),
        }),
    )
    # Função para criar um novo usuário
    def save_model(self, request, obj, form, change):
        obj.set_password(form.cleaned_data['senha'])  # Salva a senha corretamente
        super().save_model(request, obj, form, change)  # Ordenação padrão

class CadastroTarefasAdmin(admin.ModelAdmin):
    list_display = ('titulo_tarefa', 'responsavel', 'status', 'data', 'datadoregistro')  # Campos a serem exibidos na lista
    list_filter = ('status', 'responsavel')  # Filtros na lateral
    search_fields = ('titulo_tarefa', 'descricao')  # Campos pesquisáveis
    ordering = ('-datadoregistro',)  # Ordenação por data de registro

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(CadastroTarefas, CadastroTarefasAdmin)
