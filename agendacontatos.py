
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


lista_contato = []
while True:
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
    elif opcao == 0:
        break