from django.urls import path
from .views import UserList, UserDetail, UserUpdate, UserDelete

urlpatterns = [
    # Define as URLs para cada view
    path('users/', UserList.as_view(), name='user-list'),  # Lista todos os usuários e permite criar novos usuários
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # Exibe os detalhes de um usuário específico
    path('users/<int:pk>/update/', UserUpdate.as_view(), name='user-update'),  # Permite atualizar os dados de um usuário
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),  # Permite excluir um usuário
]
