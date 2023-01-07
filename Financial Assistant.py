import math
import os
os.system("cls")
import time



nome = str(input('Óla, Digite seu nome: ')).title().strip()
cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m','verde':'\033[;32m', 'fim':'\033[m', 'amarelo': '\033[;33m'}
print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))

def menu():

    print('1 = criar um novo banco de dados.\n')
    print('2 = ver saldo \n')
    print('3 = abrir banco de dados e adicionar valores \n')
    print('4 = abrir banco de dados e adicionar dispesas ou remover valor \n')
    print('5 = finalizar programa \n')
    print(" ")
    action = int(input())
    os.system('cls')
    if action == 1:
        new_database()
    elif action == 2:
        open_database()
    elif action == 3:
        add_value()
    elif action == 4:
        add_expenses()
    elif action == 5:
        finish()
    else:
        print('[!] ERRO opção invalida, escolha uma opção valida.')
        menu()

def new_database():
    os.system ('cls')
    bank_base = open('carteira.txt', 'w')
    print('[+] Criando banco de dados . . .\n')
    bank_base.write(str('00.00'))
    bank_base.close()
    time.sleep(1.5) 
    print('[+] banco de dados com sucesso !!\n')
    print('[+] voltando ao menu . . .')
    time.sleep(1.5)
    menu()

def open_database():
    try:
        os.system ('cls')
        print('[+] Verificando valor disponivel . . . ')
        time.sleep(1.5)
        with open('carteira.txt', 'r') as arquivo:
            wallet = arquivo.read()
            print('\nSaldo disponivel é de: €{} Euros.\n'.format(wallet))
            wallet = float(wallet)
            return wallet
    except:
        print('\n[!] Nenhum banco de dados encontrato.\n'
        '\n[!] Escolha a opção [1] no menu para criar um banco de dados.\n'
        '\n[+] Voltando ao menu . . . ')
        time.sleep(4)
        print(' ')
        menu()


def add_value():
    wallet = open_database()
    valor = float(input('Digite o valor: '))
    
    if valor == 0:
        print('[+] Nenhum valor adicionado ! ! !')
    elif valor > 0:
        add_values = wallet + valor

    elif valor < 0:
        print('[!] ATENÇÃO !!!'
        '\n[!] Valor negatigo significa dispesa, volte ao menu e escolha a: "OPÇÃO [ 4 ], '
        'para adicionar uma nova dispesa.\n')
        açao = str(input("Quer voltar ao menu para escolher a opção ?" "[y/n]: ")).strip().title()
        if açao == 'Y':
            print('\n[+] Voltando ao menu inicial. . .')
            time.sleep(1.5)
            print(' ')

            menu()
        else:
            while açao != 'Y':
                print('[!] OPÇÃO INVALIDA !!! \n')
                açao = str(input("escola opção 'y' para voltar ")).strip().title()
                print(' ')
                menu()
    else:
        print('\n[!] OPÇÃO INVALIDA ')
        print('\n[!] DIGITE UM VALOR VALIDO PARA CONTINUAR.')
    
    
    print('\n[+] Adicionando valor . . .')
    time.sleep(1.5)
    bank_base = open('carteira.txt', 'w')
    bank_base.write(str("{:.2f}".format(add_values)))
    bank_base.close
    print('\n[+] Valor adicionado com SUCESSO !!')
    print('\n[+] Valor total agora disponivel é de: €{:.2f} Euros.\n'.format(add_values))
    


def add_expenses():
    print('[+] Verificando valor disponivel . . . ')
    time.sleep(1.5)
    with open('carteira.txt', 'r') as arquivo:
        wallet = arquivo.read()
        print('\n[+] Saldo da carteira é de: €{} Euros'.format(wallet))

    wallet = float(wallet)
    expense = str(input('\nadicionar dispesa? s ou n ?: ')).strip().lower()
    while expense == 's':
        try: 
            name_expense =  str(input('\nDigite o nome da da dispesa para registrar: ')).title().strip()
            valor = float(input('\nQual o valor vai retirar para: {}{}{} ?: '.format(cores['amarelo'],name_expense,cores['fim'])))
            if valor < 0:
                print('\n[!] ERROR, dispesas tem que ser valor acima de $ 0,00 ')
                print('\n[+] Caso não deseje adicionar mais nenhuma dispesa volte ao menu.')
                escolha = str(input('\n[+] DESEJA VOLTAR AO MENU INICIAL ? (s) / (n)\n')).strip().lower()
                if escolha == 's':
                    menu()
                else:
                    continue
            else:
                print('[+] registrando  dispesa . . .')
                time.sleep(1.5)
                porcentagem = 100 * valor / wallet
                wallet = wallet - valor 
                print('[+] Dispesa registrada com SUCESSO !!')
                time.sleep(0.7)
                print('\n[+] Temos disponivel na carteira valor total de: €{}{:.2f}{}'.format(cores['azul'], wallet, cores['fim']))
                print('[+] A porcentagem da dispesa, {}{}{}, é de: {}{:.2f}{} %, do saldo total.'.format(cores['amarelo'], name_expense, cores['fim'], cores['verde'], porcentagem, cores['fim']))
                expense = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
        except:
            print("[!] ERROR: NÃO É PERMITIDO ('ALPHABET E SIMBOLOS') NESTA OPÇÃO;")

    else:
        print('\nok, {}{}{}: temos disponivel na carteira valor total de: €{}{:.2f}{}\n'.format(cores['roxo'],nome,cores['fim'],cores['azul'],wallet,cores['fim']))
        print('[+] Abrindo banco de dados . . .')
        time.sleep(1.5)
        print('[+] Salvando valor final . . .')
        time.sleep(1.5)
        bank_base = open('carteira.txt', 'w')
        bank_base.write(str("{:.2f}".format(wallet)))
        bank_base.close()
        print('[+]','#'*3, 'Valor já salvo no banco de dados !!', '#'*3, '\n')

def finish():
    print('[+] Encerrando o programa ...')
    time.sleep(1.5)
    print('[+] Programa encerrado.\n')

menu()
#print('\n\33[7;30;41mPrograma ainda em desenvolvimento\... \33[m')
