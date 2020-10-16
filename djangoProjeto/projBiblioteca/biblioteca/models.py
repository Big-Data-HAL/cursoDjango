from django.db import models

# Create your models here.
class Livro(models.Model):
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    isbn = models.IntegerField(default=0)
    numeroPaginas = models.IntegerField(default=0)
    titulo = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField(default=0)
    emailEditora = models.EmailField(max_length=50)
