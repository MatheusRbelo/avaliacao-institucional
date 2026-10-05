from django.urls import path
from . import views

urlpatterns = [
    # As rotas mais especificas vem antes da lista geral.
    path('avaliacoes/pendentes/', views.listar_pendentes, name='listar_pendentes'),
    path('avaliacoes/resumo/', views.resumo_por_disciplina, name='resumo_por_disciplina'),
    path('avaliacoes/', views.listar_avaliacoes, name='listar_avaliacoes'),
]
