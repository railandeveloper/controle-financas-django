from django.shortcuts import render, redirect
from .models import Lancamento
from .forms import LancamentoForm

def listar_dividas(request):
    dividas = Lancamento.objects.all()
    return render(request, 'listar_dividas.html', {'dividas': dividas})

def cadastrar_dividas(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dividas')
    else:
        form = LancamentoForm()
    return render(request, 'cadastrar_dividas.html', {'form': form})
