from django.urls import path
from . import views

urlpatterns = [
    path('novo_ctn/', views.novo_ctn, name="novo_ctn"),
    path('ctn', views.ctn, name="ctn"),
    path('ctn/<int:id>', views.ctn_unico, name="ctn_unico"),
    path('ctn/excluir/<int:id>', views.ctn_excluir, name="ctn_excluir"),
    path('ctn/busca', views.busca, name="busca"),
    
]