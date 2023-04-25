from django.shortcuts import render

# Importa as classes ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView e DestroyAPIView da biblioteca rest_framework
from rest_framework import generics

# Importa o modelo User do arquivo models.py
from .models import User

# Importa a classe UserSerializer do arquivo serializers.py
from .serializers import UserSerializer

# Define a classe UserList que herda de ListCreateAPIView
class UserList(generics.ListCreateAPIView):
    # Define a query para todos os objetos User
    queryset = User.objects.all()
    # Define o serializer usado pela classe
    serializer_class = UserSerializer

# Define a classe UserDetail que herda de RetrieveUpdateDestroyAPIView
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # Define a query para todos os objetos User
    queryset = User.objects.all()
    # Define o serializer usado pela classe
    serializer_class = UserSerializer

    # Sobrescreve o método delete da classe
    def delete(self, request, *args, **kwargs):
        # Chama o método destroy() da classe para deletar o objeto correspondente
        return self.destroy(request, *args, **kwargs)

# Define a classe UserUpdate que herda de UpdateAPIView
class UserUpdate(generics.UpdateAPIView):
    # Define a query para todos os objetos User
    queryset = User.objects.all()
    # Define o serializer usado pela classe
    serializer_class = UserSerializer

# Define a classe UserDelete que herda de DestroyAPIView
class UserDelete(generics.DestroyAPIView):
    # Define a query para todos os objetos User
    queryset = User.objects.all()
    # Define o serializer usado pela classe
    serializer_class = UserSerializer
