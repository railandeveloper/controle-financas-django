from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['descricao', 'valor', 'tipo', 'data', 'categoria', 'vencimento']
        
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")
        return valor    
