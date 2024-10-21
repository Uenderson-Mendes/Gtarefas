from django.urls import path # type: ignore
from . import views  # Importe suas views aqui

urlpatterns = [
    path('adicionar/', views.adicionar_tarefa, name='adicionar'),
    path('detalhar/<int:tarefa_id>/', views.detalhe_tarefa, name='detalhar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('excluir/<int:tarefa_id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('add_usuario/', views.add_usuario, name='add_usuario'),
    path('adicionar_tarefa/', views.add_tarefa_view, name='adicionar_tarefa'),
    path('detalhes_usuarios/', views.detalhes_usuarios, name='detalhes_usuarios'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('deletar_usuario/<int:usuario_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar_usuario/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('editar_tarefa/<int:tarefa_id>/', views.detalhe_tarefa, name='editar_tarefa'),  # Para editar tarefa individual
    path('detalhes_usuarios/', views.detalhes_usuarios, name='detalhes_usuarios'),
    
]
