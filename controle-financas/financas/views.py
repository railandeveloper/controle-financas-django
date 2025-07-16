from django.shortcuts import render, redirect
from .models import Lancamento
from .forms import LancamentoForm

def listar_dividas(request):
    filtro = request.GET.get('filtro', 'abertas')  # muda o padrão para mostrar só abertas

    if filtro == 'pagas':
        dividas = Lancamento.objects.filter(foi_pago=True)
    elif filtro == 'abertas':
        dividas = Lancamento.objects.filter(foi_pago=False)
    else:
        dividas = Lancamento.objects.filter(foi_pago=False)  # para qualquer outro caso, só abertas

    total_dividas = sum(divida.valor for divida in dividas if not divida.foi_pago)
    
    return render(request, 'listar_dividas.html', {
        'dividas': dividas,
        'total_dividas': total_dividas,
        'filtro': filtro
    })

    


def cadastrar_dividas(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dividas')
    else:
        form = LancamentoForm()
    return render(request, 'cadastrar_dividas.html', {'form': form})


def pagar_divida(request, id):
    divida = Lancamento.objects.get(id=id)
    divida.foi_pago = True
    divida.save()
    return redirect('listar_dividas')

