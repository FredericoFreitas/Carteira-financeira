nome = str(input('Óla, Digite seu nome: ')).title().strip()
cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m','verde':'\033[;33m', 'fim':'\033[m'}
print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))
print('A partir de agora vou te auxiliar na sua gestão financeira ok.')

ordenado = float(input('\nDigite o valor do seu ordenado: '))
print('\n{}OBS: !!!{}''Em portugal normalmente a conta de luz e gás são juntas e outras separas.'.format(cores['red'], cores['fim']))
gaseluz = str(input('A sua fatura é junta? s ou n ?: ')).strip()

if gaseluz == 's':

    luzegas = float(input('\nDigite o valor total da sua fatura: '))
    valor = luzegas
    porcentagem = 100 * valor / ordenado
    print('A porcentagem da dispesa de luz e gás é de: {:.2f} %'.format(porcentagem))
else:
    luz = float(input('\nDigite o valor da fatura de Luz: '))
    gas = float(input('Digite o valor que costuma comprar o gás: '))
    valor = luz+gas
    porcentagem = 100 * valor / ordenado
    print('A porcentagem da dispesa de luz e gás é de: {:.2f} %'.format(porcentagem))

água = float(input('\nDigite o valor da fatura de água: '))
porcentagem = 100 * água / ordenado
print('A porcentagem da dispesa de água é de: {:.2f} %'.format(porcentagem))

renda = float(input('\nDigite o valor da renda/Aluguel: '))
porcentagem = 100 * renda / ordenado
print('A porcentagem da dispesa de Aluguel é de: {:.2f} %'.format(porcentagem))

internet = str(input('\nVoçê possui algum plano de internet em casa? s ou n ?: ')).strip()
if internet == 's':
    net = float(input('Digite o valor da fatura: '))
    porcentagem = 100 * net / ordenado
    print('A porcentagem da dispesa de internet é de: {:.2f} %'.format(porcentagem))
else:
    print('')

if gaseluz == 's':
    dispesa = (ordenado - luzegas - água)

else:
    dispesa = (ordenado - luz - gas - água)


if internet == 's':
    dispesa = (ordenado - valor - água - net - renda)
    total = dispesa
    porcentagem = 100 * total / ordenado
    print('\nO valor do seu ordenado: ${}{:.2f}{}, menos: luz, gás, água e internet é de: ${}{:.2f}{} '.format(cores['azul'],ordenado,cores['fim'],cores['azul'],total,cores['fim']))
    print('A porcentagem total das dispesas é de: {:.2f} %'.format(porcentagem))
else:
    dispesa = (ordenado - valor - água - renda)
    total = dispesa
    porcentagem = 100 * total / ordenado
    print('O valor do seu ordenado: ${}{:.2f}{}, menos: luz, gás e água, aluguel é de: ${}{:.2f}{} '.format(cores['azul'],ordenado,cores['fim'],cores['azul'],total,cores['fim']))
    print('A porcentagem total das dispesas é de: {:.2f} %'.format(porcentagem))

açao = str(input('\nVai querer adicionar mais alguma dispesa? s ou n ?: ')).strip()
if açao == 's':
    variavel = str(input('\nDigite o nome da da dispesa para registrar: ')).title().strip()
    nome = variavel
    valor = float(input('\nQual o valor vai retirar para: {}{}{}?: '.format(cores['verde'],nome,cores['fim'])))
    valor_da_açao = total - valor
    porcentagem = 100 * valor / ordenado
    print('Foi retirado: ${}{:.2f}{}, para {}{}{}, restando na carteira o valor de: ${}{:.2f}{}'.format(cores['azul'],valor,cores['fim'],cores['verde'],nome,cores['fim'],cores['azul'],valor_da_açao,cores['fim']))
    print('A porcentagem da dispesa, {}, é de: {:.2f} %'.format(nome, porcentagem))
else:
    print('\nok, {}{}{}: temos na carteira valor total de: ${}{:.2f}{}'.format(cores['roxo'],nome,cores['fim'],cores['azul'],total,cores['fim']))


print('\33[7;30;41mPrograma ainda em desenvolvimento\... \33[m')
