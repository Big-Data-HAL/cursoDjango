from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^livro_list/', livro_list, name='listar_livros'),
    url(r'livro_new/',livro_new, name='livro_new')
]