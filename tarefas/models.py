from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, cpf, nome_user, password=None):
        if not cpf:
            raise ValueError("O CPF deve ser fornecido")
        if not nome_user:
            raise ValueError("O nome deve ser fornecido")

        usuario = self.model(cpf=cpf, nome_user=nome_user)
        usuario.set_password(password)  # Use 'set_password' para criptografar a senha
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, cpf, nome_user, password=None):
        usuario = self.create_user(cpf, nome_user, password)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=11, unique=True)
    nome_user = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome_user']  # Inclua apenas campos obrigatórios adicionais

    def __str__(self):
        return f"{self.nome_user} (CPF: {self.cpf})"



class CadastroTarefas(models.Model):
    STATUS_CHOICES = [
        ('Aberta', 'Aberta'),
        ('Pendente', 'Pendente'),
        ('Executada', 'Executada'),
    ]

    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relacionamento com o usuário
    data = models.DateField()  # Data da tarefa
    titulo_tarefa = models.CharField(max_length=200)  # Título da tarefa
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='Aberta')  # Status da tarefa
    datadoregistro = models.DateField(auto_now_add=True)  # Data do registro do tempo
    horas_trabalhadas = models.DurationField()  # Horas ou minutos trabalhados
    descricao = models.TextField()  # Descrição do trabalho realizado

    def __str__(self):
        return f"Tarefa: {self.titulo_tarefa} - {self.get_status_display()} ({self.responsavel.nome_user})"

    def save(self, *args, **kwargs):
        # Se a data da tarefa for anterior à data de hoje e o status estiver vazio, marca como pendente
        if self.data < date.today() and not self.status:
            self.status = 'Pendente'
        super(CadastroTarefas, self).save(*args, **kwargs)  # Chama o método save original
