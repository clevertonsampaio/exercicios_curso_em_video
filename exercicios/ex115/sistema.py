from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessos.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do didtema.
        cabeçalho('saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(2)

