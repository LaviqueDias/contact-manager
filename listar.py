def listar_contatos(lista):
    lista_organizada = ""
    for contato in lista:
        lista_organizada += "Contato:\n"
        for chave, valor in contato.items():
            lista_organizada += f"{chave}: {valor}\n"
        lista_organizada += "\n"

    return lista_organizada