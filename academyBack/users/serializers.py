# Importa a classe "serializers" da biblioteca "rest_framework"
from rest_framework import serializers

# Importa o modelo "User" da aplicação
from .models import User

# Define a classe "UserSerializer" que herda da classe "ModelSerializer"
class UserSerializer(serializers.ModelSerializer):
    # Define a classe Meta
    class Meta:
        # Define o modelo a ser serializado
        model = User
        # Define os campos a serem serializados (todos, no caso)
        fields = '__all__'
