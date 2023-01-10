from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import constants
from .models import movimentos
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from .validador import valid


# Create your views here.

@login_required(login_url="/")
@permission_required("mov_ctn.add_movimentos")
def novo_ctn(request):
    if request.method == 'GET':
        return render(request, 'novo_ctn.html')
    elif request.method == 'POST':

        current_user = request.user
        user_login = current_user.username

        container = request.POST.get('container')
        unidade = request.POST.get('unidade')
        tipo = request.POST.get('tipo')
        lacre = request.POST.get('lacre')
        modal = request.POST.get('modal')
        estado = request.POST.get('estado')
        obvserv = request.POST.get('observ')
        data_entrada = request.POST.get('data_entrada')

        movimento_find = movimentos.objects.filter(data_saida__isnull = True, container=container)
        
               
        if (movimento_find):
            
            messages.add_message(request, constants.ERROR, 'Container já está no terminal.')
            return redirect ('/mov/novo_ctn/')            

        if valid(container) == False:
            messages.add_message(request, constants.ERROR, 'Número de container inválido')
            return redirect ('/mov/novo_ctn/')

        if (unidade == None or tipo == None or modal == None or estado == None or len(lacre.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Obrigatório o preenchimento de todos os campos')
            return redirect ('/mov/novo_ctn/')
        
     
        movimento = movimentos(
                container = container,
                unidade = unidade,
                tipo = tipo,
                lacre = lacre,
                modal = modal,
                estado = estado,
                observ = obvserv,
                data_entrada = data_entrada,
                usuario_inclusao = user_login)
        
        movimento.save()
        messages.add_message(request, constants.SUCCESS, 'Entrada do container realizada com sucesso.')
        

        return redirect('/mov/ctn')

@login_required(login_url="/")
@permission_required("mov_ctn.view_movimentos")
def ctn(request):

    movimento_filtrar = request.GET.get('filtrar')
    movimento = movimentos.objects.filter(data_saida__isnull = True)

    if movimento_filtrar:
        movimento = movimento.filter(container__icontains = movimento_filtrar)

    return render(request, 'ctn.html', {'movimento': movimento})


@login_required(login_url="/")
@permission_required("mov_ctn.change_movimentos")
def ctn_unico(request, id):
    ctn_unico = get_object_or_404(movimentos, id=id) #data_saida__isnull = True)
    
    if request.method == 'GET':
        return render(request, 'ctn_unico.html', {'ctn': ctn_unico})
    

    
    elif request.method == 'POST':

        if not ctn_unico.data_saida is None:
            messages.add_message(request, constants.ERROR, 'Não é possível efetuar uma nova saída do container')
            return redirect(f'/mov/ctn/{id}')
        
        current_user = request.user
        user_login = current_user.username

        ctn_unico.data_saida = timezone.now()
        ctn_unico.usuario_alteracao = user_login

        ctn_unico.save()
        messages.add_message(request, constants.SUCCESS, 'Efetuada a saída do container')
        return redirect(f'/mov/ctn/{id}')


@login_required(login_url="/")
@permission_required("mov_ctn.delete_movimentos")   
def ctn_excluir(request, id):

    ctn_excluir = movimentos.objects.get(id=id)

    if not ctn_excluir.data_saida is None:
        messages.add_message(request, constants.ERROR, 'Não é possível excluir um container com data de saída')
        return redirect(f'/mov/ctn/{id}')


    ctn_excluir.delete()
    messages.add_message(request, constants.WARNING, 'Container excluído com sucesso')
    return redirect('/mov/ctn')


@login_required(login_url="/")
@permission_required("mov_ctn.view_movimentos")
def busca(request):
    
    container_filter = request.GET.get('container')
    datini_filter = request.GET.get('data_ini')
    datfin_filter = request.GET.get('data_fin')
    estado_filter = request.GET.get('estado')
    unidade_filter = request.GET.get('unidade')
    inside_filter = request.GET.get('inside')
    
    movimento = movimentos.objects.filter()

    if container_filter:
        movimento = movimento.filter(container__icontains = container_filter)

    if unidade_filter:
        movimento = movimento.filter(unidade = unidade_filter)

    if estado_filter:
        movimento = movimento.filter(estado = estado_filter)

    if datini_filter != "" and datfin_filter == "" or datini_filter == "" and datfin_filter != "":
        messages.add_message(request, constants.ERROR, 'Para busca com data é necessário informar a data inicial e final')
        return redirect('/mov/ctn/busca')    

    if datini_filter and datfin_filter:
        movimento = movimento.filter(data_entrada__range = (datini_filter, datfin_filter))


    if inside_filter:
        movimento = movimento.filter(data_saida__isnull = True)


    if not movimento:
        messages.add_message(request, constants.WARNING, 'Nenhum resultado encontrado para esta busca')
        

    return render(request, 'busca.html', {'movimento': movimento})


## teste teste 2







