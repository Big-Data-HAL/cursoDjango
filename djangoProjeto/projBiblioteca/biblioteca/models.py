import datetime
from django.db import models
from datetime import datetime
start_date = datetime(2020,12,1)
end_date = datetime(2020,12,30)

# Create your models here.
class Livro(models.Model):
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    isbn = models.IntegerField(default=0)
    numeroPaginas = models.IntegerField(default=0)
    titulo = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField(default=0)
    emailEditora = models.EmailField(max_length=50)
    # dataCadastro = models.DateTimeField('date published')
    dataCadastro = models.DateTimeField(default=datetime.now(), blank=True)

class MlTeca(models.Model):
    paginas = models.IntegerField(default=0)
    publicacao = models.IntegerField(default=0)
    assunto = models.IntegerField(default=0)
    avaliacao = models.IntegerField(default=0)

    # class Meta:
        # db_table = 'Livro'

    #
    # def __str__(self):
        # return  self.titulo

