
# Função utilizada para adicionar contatos
def adicionar_contato(lista_contato, nome_contato, telefone, email):
    contatos = {
        "nome": nome_contato,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    lista_contato.append(contatos)
    print(f"\nContato {nome_contato} foi adicionado com sucesso!\n")
    return


# Função utilizada para visualizar lista de contatos
def ver_contatos(lista_contato):
    print("\n" + "="*30)
    print(f"{'LISTA DE CONTATOS':^30}")
    print("="*30)
    for indice, contatos in enumerate(lista_contato, start=1):
        favorito = '★' if contatos["favorito"] else ""
        nome_contato = contatos["nome"]
        telefone = contatos["telefone"]
        email = contatos["email"]
        print(f"{indice}. {favorito} {nome_contato}")
        print(f"    Telefone: {telefone}")
        print(f"    E-mail  : {email}")
        print("-" * 30)
    return


# Função utilizada para editar um contato adicionado utilizando seu índice como parâmetro
def editar_contato(lista_contato, indice_contato, novo_nome_contato, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contato):
        lista_contato[indice_contato_ajustado]["nome"] = novo_nome_contato
        lista_contato[indice_contato_ajustado]["telefone"] = novo_telefone
        lista_contato[indice_contato_ajustado]["email"] = novo_email
    else:
        print("Índice de contato incorreto!")
    return


# Função utilizada para excluir um contato utilizando seu índice como parâmetro
def excluir_contato(lista_contato, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contato):
        del (lista_contato[indice_contato_ajustado])
        print("Contato excluído com sucesso!")
    else:
        print("Índice de contato incorreto!")
    return


# Função utilizada para marcar contato como favorito utilizando seu índice como parâmetro
def favoritar_contato(lista_contato, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contato):
        lista_contato[indice_contato_ajustado]["favorito"] = True
        print("Contato favoritado com sucesso!")
    else:
        print("Índice de contato incorreto!")
    return


def ver_contatos_favoritos(lista_contato):
    print("\n" + "="*30)
    print(f"{'CONTATOS FAVORITOS':^30}")
    print("="*30)
    for indice, contatos in enumerate(lista_contato, start=1):
        favorito = '★' if contatos["favorito"] else ""
        nome_contato = contatos["nome"]
        telefone = contatos["telefone"]
        email = contatos["email"]
        print(f"{indice}. {favorito} {nome_contato}")
        print(f"    Telefone: {telefone}")
        print(f"    E-mail  : {email}")
        print("-" * 30)
    return


def desfavoritar_contato(lista_contato, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contato):
        lista_contato[indice_contato_ajustado]["favorito"] = False
        print("Contato exclu[ido dos favoritos!")
    else:
        print("Índice de contato incorreto!")
    return


lista_contato = []
while True:
    print("\n" + "="*50)
    print(f"{'MENU DE OPÇÕES':^50}")
    print("="*50)
    print("[1] - Adicionar contato")
    print("[2] - Visualizar lista de contatos")
    print("[3] - Editar contato")
    print("[4] - Excluir contato")
    print("[5] - Marcar contato como favorito")
    print("[6] - Visualizar lista de contatos favoritos")
    print("[7] - Desmarcar contato como favorito")
    print("[0] - Sair")
    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        nome_contato = str(input("Nome: "))
        telefone = str(input("Telefone: "))
        email = str(input("E-mail: "))
        adicionar_contato(lista_contato, nome_contato, telefone, email)
    elif opcao == 2:
        ver_contatos((lista_contato))
    elif opcao == 3:
        ver_contatos(lista_contato)
        indice_contato = int(input("Digite o número do contato que desejada editar: "))
        novo_nome_contato = str(input("Digite o novo nome: "))
        novo_telefone = str(input("Digite o novo número de telefone: "))
        novo_email = str(input("Digite o novo e-mail: "))
        editar_contato(lista_contato, indice_contato, novo_nome_contato, novo_telefone, novo_email)
    elif opcao == 4:
        ver_contatos(lista_contato)
        indice_contato = int(input("Digite o número do contato que deseja excluir: "))
        excluir_contato(lista_contato, indice_contato)
    elif opcao == 5:
        ver_contatos(lista_contato)
        indice_contato = int(input("Digite o número do contato que desejada favoritar: "))
        favoritar_contato(lista_contato, indice_contato)
    elif opcao == 7:
        ver_contatos(lista_contato)
        indice_contato = int(input("Digite o número do contato que desejada remover dos favoritos: "))
        desfavoritar_contato(lista_contato, indice_contato)
    elif opcao == 0:
        break
