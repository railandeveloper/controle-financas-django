from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_dividas, name='listar_dividas'),
    path('nova/', views.cadastrar_dividas, name='cadastrar_dividas'),
]
