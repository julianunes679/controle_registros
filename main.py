def menu_registros():
    print("===MENU===")
    print("SISTEMA DE REGISTRO")
    print("1 - ")
    print("2 - ")  
    print("3 - Sair")

def opcao_um():
    print("Excecutando opção 1")
def opcao_dois():
    print("Excecutando opção 2")

def controle ():
    while True:     
        menu_registros()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            opcao_um()
        elif opcao == "2":
            opcao_dois()
        elif opcao == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

controle()