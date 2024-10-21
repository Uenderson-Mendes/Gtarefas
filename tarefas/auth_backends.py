from django.contrib.auth.backends import ModelBackend # type: ignore
from .models import Usuario

class CPFBackend(ModelBackend):
    def authenticate(self, request, cpf=None, senha=None, **kwargs):
        try:
            user = Usuario.objects.get(cpf=cpf,senha=senha)
            # Aqui você pode implementar a lógica de autenticação, por exemplo,
            # validando a senha. Para simplificação, assumimos que apenas o CPF é necessário.
            return user
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
