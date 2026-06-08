# abora importar os comandos do sistema operacional
import os

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

def finalizar_app():
    os.system('cls')  # Limpa a tela do terminal
    print("""

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━╮╭━━┳━━┳━┳━┳━━┳━╮╭━╯┣━━╮╭━━┳━┳━━┳━━┳━┳━━┳╮╭┳━━╮
┃╭━━┫╭╮┫╭━┫┃━┫╭┫╭┫╭╮┃╭╮┫╭╮┃╭╮┃┃╭╮┃╭┫╭╮┃╭╮┃╭┫╭╮┃╰╯┃╭╮┃
┃╰━━┫┃┃┃╰━┫┃━┫┃┃┃┃╭╮┃┃┃┃╰╯┃╰╯┃┃╰╯┃┃┃╰╯┃╰╯┃┃┃╭╮┃┃┃┃╭╮┃
╰━━━┻╯╰┻━━┻━━┻╯╰╯╰╯╰┻╯╰┻━━┻━━╯┃╭━┻╯╰━━┻━╮┣╯╰╯╰┻┻┻┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╱╱╱╱╱╰━━╯
          
          """)

def escolher_opcao():
    opcao_escolhida = int(input('Digite a opção desejada: '))
# outro jeito seria opcao_escolhida = int(opcao_escohida) para converter a string digitada pelo usuário em um número inteiro, mas o jeito mais recomendado é usar o int() para garantir que a variável seja do tipo inteiro.

# tinha isso antes... print(f'Opção escolhida: {opcao_escolhida}') esse é um dos jeitos de interpolar strings, outro seria usar "string"{variavel}"string" e concatenar usando o sinal de +, mas o jeito mais recomendado é usar o f-string, que é mais legível e fácil de usar.

# print(type(opcao_escolhida)) # para verificar o tipo da variável, que é string.
# print(type(1)) # para verificar o tipo do número 1, que é inteiro.

    if opcao_escolhida == 1:
        print('Opção 1 escolhida: Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Opção 2 escolhida: Listar restaurante')
    elif opcao_escolhida == 3:
        print('Opção 3 escolhida: Ativar restaurante')  
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
