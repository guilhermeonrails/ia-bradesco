# -*- coding: utf-8 -*-

import json
import os

ARQUIVO_USUARIOS = 'usuarios.json'

def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    try:
        with open(ARQUIVO_USUARIOS, 'r') as f:
            return json.load(f)
    except:
        print "Erro ao ler o arquivo de usuarios. Criando novo arquivo."
        return []

def salvar_usuarios(usuarios):
    try:
        with open(ARQUIVO_USUARIOS, 'w') as f:
            json.dump(usuarios, f, indent=4)  # identado e formatado
    except:
        print "Erro ao salvar os dados de usuarios."

def cadastrar_usuario():
    print "=== Cadastro de Usuário ==="
    nome = raw_input("Digite o nome do usuário: ")
    idade = raw_input("Digite a idade do usuário: ")
    email = raw_input("Digite o email do usuário: ")


    usuarios = carregar_usuarios()

    # Verificar se o usuário já existe (pelo nome)
    for u in usuarios:
        if u['nome'] == nome:
            print "Erro: Usuário já cadastrado!"
            return

    novo_usuario = {'nome': nome, 'idade': idade, 'email': email}
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    print "Usuário cadastrado com sucesso!"

def listar_usuarios():
    print "\n=== Lista de Usuários Cadastrados ==="
    usuarios = carregar_usuarios()

    if len(usuarios) == 0:
        print "Nenhum usuário cadastrado."
    else:
        for u in usuarios:
            print "Nome: " + u['nome']
            print "Idade: " + u['idade']
            print "Email: " + u['email']
            print "-------------------------"

def menu():
    while True:
        print "\n=== Menu Principal ==="
        print "1. Cadastrar Usuário"
        print "2. Listar Usuários"
        print "3. Sair"
        escolha = raw_input("Escolha uma opção: ")
        print ""

        if escolha == '1':
            cadastrar_usuario()
        elif escolha == '2':
            listar_usuarios()
        elif escolha == '3':
            print "Saindo do sistema..."
            break
        else:
            print "Opção inválida. Tente novamente."

if __name__ == '__main__':
    menu()
