from django.db import models
import datetime


# Create your models here.
# financas/models.py


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Lancamento(models.Model):
    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesa'),
    )
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    foi_pago = models.BooleanField(default=False)
    vencimento = models.DateField(default=datetime.date.today)



    def __str__(self):
        return f"{self.get_tipo_display()} - {self.descricao} - R$ {self.valor}"
