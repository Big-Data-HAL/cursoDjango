import django_filters
from .models import Livro

class LivroFilters(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains')
    dataCadastro = django_filters.DateFilter(lookup_expr='icontains')

    class Meta:
        model = Livro
        fields = ('titulo', 'dataCadastro')