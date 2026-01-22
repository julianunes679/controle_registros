registros = {}

def menu_registros():
    print("===MENU===")
    print("SISTEMA DE REGISTRO")
    print("1 - Cadastro de Registro")
    print("2 - Listar Registros")  
    print("3 - Sair")

def opcao_um():
    nome = input("Nome: ")
    idade = input("Idade: ")

    registros[nome] = {
        "idade": idade
    }

    return "Cadastro realizado com sucesso"


def opcao_dois():
    if len(registros) == 0:
        return "Nenhum registro encontrado."
    else:
        for nome, dados in registros.items():
            print(f"Nome: {nome}")
            print(f"Idade: {dados['idade']}")
            print("---------------")
        return "Fim da lista de registros."


def controle ():
    while True:     
        menu_registros()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            
            resultado = opcao_um()
            print(resultado)

        elif opcao == "2":
            resultado = opcao_dois()
            print(resultado)

        elif opcao == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

controle()