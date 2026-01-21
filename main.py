registros = {}

def menu_registros():
    print("===MENU===")
    print("SISTEMA DE REGISTRO")
    print("1 - Cadastro de Registro")
    print("2 - ")  
    print("3 - Sair")

def opcao_um():
    nome = input("Nome: ")
    idade = input("Idade: ")

    registros[nome] = {
        "idade": idade
    }

    return "Cadastro realizado com sucesso"


def opcao_dois():
    return "Executando opção 2"

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