def adicionar_contato(nome, sobrenome, telefone, email, lista_contatos):
    contato = {
        'nome' : nome,
        'sobrenome' : sobrenome,
        'telefone' : telefone,
        'email' : email
    }

    ja_adicionado = False
    for contato in lista_contatos:
        if contato['telefone'] == telefone:
            ja_adicionado = True
            return ja_adicionado
    
    lista_contatos.append(contato)
    return ja_adicionado

def listar_contatos(lista):
    lista_organizada = ""
    for contato in lista:
        lista_organizada += "Contato:\n"
        for chave, valor in contato.items():
            lista_organizada += f"{chave}: {valor}\n"
        lista_organizada += "\n"

    return lista_organizada

def excluir_contato(telefone, lista_contatos):
    foi_excluido = False
    for contato in lista_contatos:
        if contato['telefone'] == telefone:
            lista_contatos.remove(contato)
            foi_excluido = True
            return foi_excluido
    return foi_excluido

        
            
        