from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^livro_list/', livro_list, name='livro_list'),
    url(r'^livro_new/',livro_new, name='livro_new'),
    url(r'^livro_edit/,(?P<pk>[0-9]+)', livro_edit, name='livro_edit'),
    url(r'^livro_remove/,(?P<pk>[0-9]+)', livro_remove, name='livro_remove'),
    url('calc/', vbo, name="cal"),
    url(r'home/', home, name="home"),
    #url('mlteca/', mlteca_input, name="mlteca_input")

]
