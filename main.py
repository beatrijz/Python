name = input('Qual é o seu nome?')
dia = input('Qual o dia em que você nasceu?')
mes = input('Qual o mês em que você nasceu?')
ano = input('Qual o ano em que você nasceu?')
mensagem = 'Olá, {}'.format(name) + ', prazer em te conhecer!'
dataNascimento = 'Data de nascimento: ' + dia + '/' + mes + '/' + ano
print(mensagem)
print(dataNascimento)
