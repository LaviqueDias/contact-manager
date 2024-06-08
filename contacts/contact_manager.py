def excluir_contato(telefone, lista_contatos):
        if telefone in telefone.contatos:
            del lista_contatos.contatos[telefone]
            print(f"Contato {telefone} excluído com sucesso.")
        else:
            print(f"Contato {telefone} não encontrado.")