from django.db import models

# Define uma classe User que herda de models.Model
class User(models.Model):
    # Define os campos que a classe irá possuir, cada um com um tipo específico
    name = models.CharField(max_length=255)  # CharField é um campo de texto
    favorite_color = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  # EmailField é um campo para emails
    pet_name = models.CharField(max_length=255)

    # Define o método __str__ para retornar o nome do usuário quando a classe for convertida para string
    def __str__(self):
        return self.name
