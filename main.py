from contacts.contact_manager import *

def main():
    lista_contatos = []
    opcao = 1

    while opcao != 4:
        print('=====SISTEMA DE CONTATOS=====\n')
        print("1. Adicionar contato")
        print("2. Listar contato")
        print("3. Remover contato")
        print("4. Sair")
        
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do contato: ')
            sobrenome = input('Digite o sobrenome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o email do contato: ')

            adicionar_contato(nome, sobrenome, telefone, email, lista_contatos)
        
        elif opcao == 2:
            lista = listar_contatos(lista_contatos)
            print(lista)
            
        elif opcao == 3:
            pass

        elif opcao != 4:
            print('Digite uma opção válida!')
        


if __name__ == '__main__':
    main()