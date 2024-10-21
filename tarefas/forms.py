from django import forms # type: ignore
from django import forms # type: ignore
from .models import CadastroTarefas
from django.contrib.auth import get_user_model # type: ignore
from .models import Usuario

class CadastroTarefasForm(forms.ModelForm):
    class Meta:
        model = CadastroTarefas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pega o usuário da lista de argumentos
        super(CadastroTarefasForm, self).__init__(*args, **kwargs)

        # Se um usuário estiver logado e for um superusuário, pré-defina o campo 'responsavel'
        if user and user.is_superuser:
            self.fields['responsavel'].queryset = Usuario.objects.filter(is_active=True)  # Filtra os usuários ativos
        else:
            self.fields['responsavel'].initial = user  # Se não for superusuário, define o responsável como o usuário logado
            self.fields['responsavel'].disabled = True  # Desabilita o campo para que não possa ser alterado
  # Desabilita o campo para que não possa ser alterado

class AtualizarTarefasForm(forms.ModelForm):
    class Meta:
        model = CadastroTarefas
        fields = ['status']




class CPFLoginForm(forms.Form):
    cpf = forms.CharField(max_length=11, label="CPF")
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")  # Adicione o campo de senha

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if len(cpf) != 11 or not cpf.isdigit():
            raise forms.ValidationError("CPF inválido.")
        return cpf
    
class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['cpf', 'nome_user', 'senha']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha'])  # Encripta a senha
        if commit:
            user.save()
        return user
 # Campos que deseja editar


class TarefaForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):  # Aceita 'user' como um argumento
        super().__init__(*args, **kwargs)  # Chama o inicializador da classe pai
        self.user = user  # Armazena o usuário, se necessário

    class Meta:
        model = CadastroTarefas
        fields = ['responsavel', 'data', 'titulo_tarefa', 'status', 'horas_trabalhadas', 'descricao']  # Sem 'datadoregistro'