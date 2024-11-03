from alteracao_BD import *
from prints import *
import time
import os


def main():
    sair = False

    while( not False):
        os.system('cls')
        menu_principal()
        op = digite_opcao()

        if op == 1:
            os.system('cls')
            inserindo_cliente()
        elif op ==2:
            os.system('cls')
            remover_cliente()
        elif op ==3:
            os.system('cls')
            main_alterar()
        elif op == 4:
            os.system('cls')
            imprimir_BD()
            input("")
        elif op == 5:
            os.system('cls')
            print_saindo()
            time.sleep(2)
            os.system('cls')
            break

        op = 0

def inserindo_cliente():
    print_inserir()

    nome = (input("Nome: "))
    email =(input("Email: "))
    senha = (input("Senha: "))
    pref = (input("Pref: "))

    lista = [1,nome,email,senha,pref]
    os.system('cls')
    print_info(lista)
    if print_confirm() == 0:
        valido = inserindo_BancoDados(nome,email,senha,pref)
        if not valido:
            print("Não foi inserido")
    else:
        print("Valores invalidados")

def remover_cliente():
    email = input("Email: ")
    senha = input("Senha: ")

    removendo_BancoDados(email,senha)

def main_alterar():

    sair=False

    while(not sair):
        os.system('cls')
        menu_alterar()
        op = int(input("Digite: "))

        if op == 1:
            os.system('cls')
            email = input("Email: ")
            senha_antiga = input("Senha Atual: ")
            senha_nova = input("Senha Nova: ")
            alterar_senha_BancoDados(email,senha_antiga,senha_nova)
        elif op == 2:
            os.system('cls')
            email = input("Email: ")
            senha = input("Senha: ")
            novo_nome = input("Novo nome: ")
            alterar_nome_BancoDados(email,senha,novo_nome)
        elif op == 3:
            os.system('cls')
            email = input("Email: ")
            senha = input("Senha: ")
            nova_pref = input("Nova Preferencia: ")
            alterar_pref_BancoDados(email,senha,nova_pref)
        elif op == 4:
            os.system('cls')
            print_saindo()
            time.sleep(1)
            break    

main()

        