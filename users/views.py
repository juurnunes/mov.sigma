from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

# @login_required(login_url="/auth/login/")
# def cadastro(request):
#     if request.method == "GET":

#         return render(request, 'cadastro.html')
    
#     elif request.method == "POST":

#         login = request.POST.get('login')
#         nome = request.POST.get('nome')
#         senha = request.POST.get('senha')

#         user = User.objects.filter(username = login)

#         if user:
#             messages.add_message(request, constants.ERROR, 'Já existe um usuário com este login')
#             return redirect('/auth/cadastro')
        
#         user = User.objects.create_user(username=login, first_name = nome, password = senha)
#         user.save()

#         messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')

#         return redirect('/auth/cadastro')


def logar(request):

    if request.method == "GET":

        return render(request, 'login.html')
    
    elif request.method == "POST":

        username = request.POST.get('login')
        senha = request.POST.get('senha')

        user = authenticate(username = username, password = senha)


        if user:

            login(request, user)
            return redirect('/mov/ctn')

        else:
            messages.add_message(request, constants.ERROR, 'Login ou senha, inválidos')
            return redirect('/')


@login_required
def sair(request):
    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado com sucesso.')
    return redirect('/')
            
