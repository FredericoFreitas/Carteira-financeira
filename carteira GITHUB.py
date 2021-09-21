nome = str(input('Óla, Digite seu nome: ')).title().strip()
cores = {'roxo':'\033[1;35m', 'azul':'\033[;34m', 'red':'\033[1;31m', 'fim':'\033[m'}
print('Hello {}{}{}!!! '.format(cores['roxo'], nome, cores['fim']))
print('A partir de agora vou te auxiliar na sua gestão financeira ok.')

ordenado = float(input('\nDigite o valor do seu ordenado: '))
print('\n{}OBS: !!!{}''Em portugal nomalmente a conta de luz e gás são juntas e outras separas.'.format(cores['red'], cores['fim']))
gaseluz = str(input('A sua fatura é junta? s ou n ? ')).strip()

if gaseluz == 's':

    luzegas = float(input('\nDigite o valor total da sua fatura: '))
    r = luzegas
else:
    luz = float(input('\nDigite o valor da fatura de Luz: '))
    gas = float(input('Digite o valor que costuma comprar o gás: '))
    r = luz+gas
água = float(input('Digite o valor da fatura de água: '))
renda = float(input('Digite o valor da renda: '))


internet = str(input('\nVoçê possui algum plano de internet em casa? s ou n? ')).strip()
if internet == 's':
    net = float(input('Digite o valor da fatura: '))
else:
    print('ok')

if gaseluz == 's':
    dispesa = (ordenado - luzegas - água)

else:
    dispesa = (ordenado - luz - gas - água)


if internet == 's':
    dispesa = (ordenado - r - água - net - renda)
    print('\nO valor do seu ordenado: ${}{:.2f}{}, menos: luz, gás, agua e internet é de: ${}{:.2f}{} '.format(cores['azul'],ordenado,cores['fim'],cores['azul'],dispesa,cores['fim']))
else:
    dispesa = (ordenado - r - água - renda)
    print('O valor do seu ordenado: ${}{:.2f}{}, menos: luz, gás e agua é de: ${}{:.2f}{} '.format(cores['azul'],ordenado,cores['fim'],cores['azul'],dispesa,cores['fim']))
