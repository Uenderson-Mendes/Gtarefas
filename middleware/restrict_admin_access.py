from django.shortcuts import redirect # type: ignore
from django.urls import reverse # type: ignore

class RestrictAdminAccessMiddleware:
    """
    Middleware to prevent non-superusers from accessing the admin panel.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o usuário está tentando acessar o admin e se ele não é superusuário
        if request.path.startswith(reverse('admin:index')):
            if not request.user.is_superuser:
                return redirect('lista_tarefas')  # Redireciona para a lista de tarefas, por exemplo
        
        response = self.get_response(request)
        return response
