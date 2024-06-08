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
    
    return ja_adicionado