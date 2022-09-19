import os
os.system("cls")
import time



nome = str(input('Óla, Digite seu nome: ')).title().strip()
cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m','verde':'\033[;32m', 'fim':'\033[m', 'amarelo': '\033[;33m'}
print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))
print('A partir de agora vou te auxiliar na sua gestão financeira ok.\n')

def menu():

    print('1 = criar um novo banco de dados.\n')
    print('2 = ver saldo \n')
    print('3 = abrir banco de dados e adicionar valores \n')
    print('4 = abrir banco de dados e adicionar dispesas ou remover valor \n')
    print('5 = finalizar programa \n')
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
    bank = open('carteira.txt', 'w')
    print('[+] Criando banco de dados . . .\n')
    bank.write(str('00.00'))
    bank.close()
    time.sleep(1.5) 
    print('[+] banco de dados com sucesso !!\n')
    print('[+] voltando ao menu . . .')
    time.sleep(1.5)
    menu()

def open_database():
    print('[+] Verificando valor disponivel . . . ')
    time.sleep(1.5)
    with open('carteira.txt', 'r') as arquivo:
        bank_str = arquivo.read()
        print('\nSaldo disponivel é de: {} Euros.\n'.format(bank_str))
        #tentar retornar valor para usar na funçao 3 do menu

def add_value():
    #tentar chamar a funçao open_database
    print('[+] Verificando valor disponivel . . . ')
    time.sleep(1.5)
    with open('carteira.txt', 'r') as arquivo:
        bank_str = arquivo.read()
        print('\nSaldo disponivel é de: {} Euros.\n'.format(bank_str))
    bank_str =float(bank_str)
    valor = float(input('Digite o valor: '))
    carteira = bank_str + valor

    if valor < 0:
        print('[!] ATENÇÃO !!!'
        '\n[!] Valor negatigo significa dispesa, volte ao menu e escolha a: "OPÇÃO [ 4 ], '
        'para adicionar uma nova dispesa.\n')
    else:
        print('\n[+] Adicionando valor . . .')
        time.sleep(1.5)
        bank = open('carteira.txt', 'w')
        bank.write(str("{:.2f}".format(carteira)))
        bank.close
        print('\n[+] Valor adicionado com SUCESSO !!')
        print('\nValor total agora disponivel é de: {:.2f} Euros.\n'.format(carteira))


def add_expenses():
    print('[+] Verificando valor disponivel . . . ')
    time.sleep(1.5)
    with open('carteira.txt', 'r') as arquivo:
        bank_str = arquivo.read()
        print('\nsaldo da carteira é de: $ {} Euros'.format(bank_str))

    bank_str = float(bank_str)
    expense = str(input('\nadicionar dispesa? s ou n ?: ')).strip()
    while expense == 's':
        name_expense =  str(input('\nDigite o nome da da dispesa para registrar: ')).title().strip()
        valor = float(input('\nQual o valor vai retirar para: {}{}{} ?: '.format(cores['amarelo'],name_expense,cores['fim'])))
        print('[+] registrando  dispesa . . .')
        time.sleep(1.5)
        porcentagem = 100 * valor / bank_str
        bank_str = bank_str - valor 
        print('temos disponivel na carteira valor total de: $ {}{:.2f}{}'.format(cores['azul'], bank_str, cores['fim']))
        print('A porcentagem da dispesa, {}{}{}, é de: {}{:.2f}{} %, do saldo total.'.format(cores['amarelo'], name_expense, cores['fim'], cores['verde'], porcentagem, cores['fim']))
        expense = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
    else:
        print('\nok, {}{}{}: temos disponivel na carteira valor total de: ${}{:.2f}{}\n'.format(cores['roxo'],nome,cores['fim'],cores['azul'],bank_str,cores['fim']))
        print('[+] Abrindo banco de dados . . .')
        time.sleep(1.5)
        print('[+] Salvando valor final . . .')
        time.sleep(1.5)
        bank = open('carteira.txt', 'w')
        bank.write(str(bank_str))
        bank.close()
        print('[+]','#'*3, 'Valor já salvo no banco de dados !!\n', '#'*3)

def finish():
    print('[+] Encerrando o programa ...')
    time.sleep(1.5)
    print('[+] Programa encerrado.')

menu()
"""
#função vai receber valor do banco de dados, somar com valor digitado, retornar a soma
def banco_de_dados(+soma):
    dinheiro = float(input('\ndigite o valor recebido: '))
    soma =  dinheiro + banco_str
    print(soma)
    return(soma)

#informaçao sobre banco de dados 
#linha 10 do arquivo correção (adicionar while neste block)
informaçao_banco = str(input("\nJá possui um banco de dados? [y] / [n] ")).strip()
if informaçao_banco == 'y':
    with open('carteira.txt', 'r') as arquivo:
        banco_str = arquivo.read()
        print('\nsaldo da carteira é de: $ {}'.format(banco_str))

    banco_str = float(banco_str)
    carteira = banco_de_dados(banco_str)
    print('valor atual total é de: {}'.format(carteira))
else:
    dinheiro = float(input('\nDigite o valor recebido: '))
    banco = open('carteira.txt', 'w')
    banco.write(str(dinheiro)) # dinheiro é a variavel que guarda resultado final
    banco.close()
    carteira = dinheiro

#adicionando novas dispesas 
açao = str(input('\nadicionar dispesa? s ou n ?: ')).strip()
while açao == 's':
    variavel = str(input('\nDigite o nome da da dispesa para registrar: ')).title().strip()
    valor = float(input('\nQual o valor vai retirar para: {}{}{}?: '.format(cores['amarelo'],variavel,cores['fim'])))
    porcentagem = 100 * valor / carteira
    carteira = carteira - valor  
    print('temos na carteira valor de total de: $ {}{:.2f}{}'.format(cores['azul'], carteira, cores['fim']))
    #print('Foi retirado: ${}{:.2f}{}, para {}{}{}, restando na carteira o valor de: ${}{:.2f}{}'.format(cores['azul'],valor,cores['fim'],cores['verde'],variavel,cores['fim'],cores['azul'],resto,cores['fim']))
    print('A porcentagem da dispesa, {}{}{}, é de: {}{:.2f}{} %'.format(cores['amarelo'], variavel, cores['fim'], cores['verde'], porcentagem, cores['fim']))
    açao = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
else:
    print('\nok, {}{}{}: temos na carteira valor total de: ${}{:.2f}{}'.format(cores['roxo'],nome,cores['fim'],cores['azul'],carteira,cores['fim']))
    print('')
    banco = open('carteira.txt', 'w')
    banco.write(str(carteira))
    print('#'*3, 'valor já salvo no banco de dados !!', '#'*3)

print('\n\33[7;30;41mPrograma ainda em desenvolvimento\... \33[m')
"""