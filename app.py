# bora importar os comandos do sistema operacional
import subprocess
restaurantes = [{'nome':'Yokan', 'categoria':'Japonesa', 'ativo':True},{ 'nome':'Sakura', 'categoria':'Japonesa', 'ativo':False},{ 'nome':'Dom Corleone', 'categoria':'Italiana', 'ativo':True}]

def exibir_nome_do_programa():
    print("""
      
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    print('1. Cadastrar restaurante\n')
    print('2. Listar restaurante\n')
    print('3. Ativar restaurante\n')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def finalizar_app():
    exibir_subtitulo("""

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━╮╭━━┳━━┳━┳━┳━━┳━╮╭━╯┣━━╮╭━━┳━┳━━┳━━┳━┳━━┳╮╭┳━━╮
┃╭━━┫╭╮┫╭━┫┃━┫╭┫╭┫╭╮┃╭╮┫╭╮┃╭╮┃┃╭╮┃╭┫╭╮┃╭╮┃╭┫╭╮┃╰╯┃╭╮┃
┃╰━━┫┃┃┃╰━┫┃━┫┃┃┃┃╭╮┃┃┃┃╰╯┃╰╯┃┃╰╯┃┃┃╰╯┃╰╯┃┃┃╭╮┃┃┃┃╭╮┃
╰━━━┻╯╰┻━━┻━━┻╯╰╯╰╯╰┻╯╰┻━━┻━━╯┃╭━┻╯╰━━┻━╮┣╯╰╯╰┻┻┻┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╰━━╯
          
          """)


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(text):
    subprocess.run('cls', shell=True)
    print(text)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes cadastrados\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'.{nome_restaurante} | {categoria} | {ativo}')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a opção desejada: '))
# outro jeito seria opcao_escolhida = int(opcao_escohida) para converter a string digitada pelo usuário em um número inteiro, mas o jeito mais recomendado é usar o int() para garantir que a variável seja do tipo inteiro.

# tinha isso antes... print(f'Opção escolhida: {opcao_escolhida}') esse é um dos jeitos de interpolar strings, outro seria usar "string"{variavel}"string" e concatenar usando o sinal de +, mas o jeito mais recomendado é usar o f-string, que é mais legível e fácil de usar.

# print(type(opcao_escolhida)) # para verificar o tipo da variável, que é string.
# print(type(1)) # para verificar o tipo do número 1, que é inteiro.

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Opção 3 escolhida: Ativar restaurante')  
        elif opcao_escolhida == 4:
            print('Opção 4 escolhida: Sair')
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    subprocess.run('cls', shell=True)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
