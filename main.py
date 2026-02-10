import json

ARQUIVO = "registros.json"


def salvar_registros():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, ensure_ascii=False, indent=4)


def carregar_registros():
    global registros
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            registros = json.load(arquivo)
    except FileNotFoundError:
        registros = {}


registros = {}
carregar_registros()


def menu_registros():
    print("\n=== SISTEMA DE REGISTRO ===")
    print("1 - Cadastro de Registro")
    print("2 - Listar Registros")
    print("3 - Sair")


def opcao_um():
    while True:
        nome_input = input("Nome: ")

        nome = nome_input.strip().lower()
        nome_formatado = nome_input.strip().title()

        if nome == "":
            print("Nome não pode ser vazio.")
        elif len(nome) < 2:
            print("Nome muito curto.")
        elif nome in registros:
            print("Esse nome já está cadastrado.")
        else:
            break

    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("Idade deve ser um número positivo.")
            else:
                break
        except ValueError:
            print("Digite uma idade válida (apenas números).")

    registros[nome] = {
        "nome": nome_formatado,
        "idade": idade
    }

    salvar_registros()
    return "Cadastro realizado com sucesso"


def opcao_dois():
    if not registros:
        return "Nenhum registro encontrado."

    for dados in registros.values():
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print("---------------")

    return "Fim da lista de registros."


def controle():
    while True:
        menu_registros()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(opcao_um())

        elif opcao == "2":
            print(opcao_dois())

        elif opcao == "3":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


controle()