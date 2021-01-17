from django.forms import ModelForm
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .bo import calculadora


# Create your views here.

def home(request, template_name='home_.html'):
    vnow = datetime.datetime.now()
    dnow = {'vnow': vnow}
    # html = "<html><body>It is now %s.</body></html>" %now
    # return HttpResponse(html)
    return render(request, template_name, dnow)


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor', 'editora', 'isbn', 'numeroPaginas', 'titulo', 'anoPublicacao', 'emailEditora', 'dataCadastro']


def livro_list(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    search = request.GET.get('search')
    if search:
        livro = livro.filter(titulo__icontains=search)
    livros = {'lista': livro}
    return render(request, template_name, livros)

# def livro_busca(request, template_name='livro_list.html'):
    # livro = Livro.objects.filter(pk=1)
    # if request.method == "POST":
        # form
    #  vbusca = {'lista': livro}
    # return render(request, template_name, vbusca)


def livro_new(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livro_list')
    return render(request, template_name, {'form': form})


def livro_edit(request, pk, template_name='livro_form.html'):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form': form})


def livro_remove(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == "POST":
        livro.delete()
        return redirect('livro_list')
    return render(request, 'livro_delete.html', {'livro': livro})


def vbo(request):
    res2 = calculadora.somar(3, 5)
    fig = calculadora.grafico()
    # html = calculadora.plotly()
    dnow = {'vnow': fig, 'vnow2': fig}
    return render(request, 'home_.html', dnow)
