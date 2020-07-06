from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=255),
    matricula = models.IntegerField(),
    senha = models.CharField(max_length=50),
    usuario = models.CharField(max_length=30)
    email = models.CharField(max_length=100)