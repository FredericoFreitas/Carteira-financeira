import os
os.system("cls")


nome = str(input('Óla, Digite seu nome: ')).title().strip()
cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m','verde':'\033[;32m', 'fim':'\033[m', 'amarelo': '\033[;33m'}
print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))
print('A partir de agora vou te auxiliar na sua gestão financeira ok.')

#função vai receber valor do banco de dados, somar com valor digitado, retornar a soma
def banco_de_dados(soma):
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
açao = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
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
